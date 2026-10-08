-- ============================================================================
-- sus-calculos.lua
-- Motor de procesamiento de datos SUS (System Usability Scale) para LuaLaTeX
-- ============================================================================

local sus = {}
sus.datos = {}
sus.stats = {}
sus.errores = {}

-- Función auxiliar para escapar caracteres especiales de LaTeX
function sus.escapar_latex(str)
    if not str then return "" end
    -- Usar marcador temporal para la barra invertida antes de procesar llaves
    str = string.gsub(str, "\\", "@@BACKSLASH@@")
    str = string.gsub(str, "%%", "\\%%")
    str = string.gsub(str, "%$", "\\$")
    str = string.gsub(str, "&", "\\&")
    str = string.gsub(str, "#", "\\#")
    str = string.gsub(str, "_", "\\_")
    str = string.gsub(str, "{", "\\{")
    str = string.gsub(str, "}", "\\}")
    str = string.gsub(str, "~", "\\textasciitilde{}")
    str = string.gsub(str, "%^", "\\textasciicircum{}")
    str = string.gsub(str, "@@BACKSLASH@@", "\\textbackslash{}")
    return str
end

-- Función auxiliar para formatear números con coma decimal (español)
function sus.formato_decimal(num, decimales)
    if not num then return "" end
    decimales = decimales or 1
    local fmt = string.format("%." .. decimales .. "f", num)
    return (fmt:gsub("%.", ","))
end

-- Parser simple de líneas CSV respetando comillas dobles
local function parse_csv_line(line)
    local campos = {}
    local c = 1
    local longitud = #line
    while c <= longitud do
        if line:sub(c, c) == '"' then
            local fin = line:find('"', c + 1)
            while fin and line:sub(fin + 1, fin + 1) == '"' do
                fin = line:find('"', fin + 2)
            end
            if not fin then fin = longitud end
            local val = line:sub(c + 1, fin - 1):gsub('""', '"')
            table.insert(campos, val)
            c = fin + 2
        else
            local fin = line:find(',', c)
            if not fin then fin = longitud + 1 end
            local val = line:sub(c, fin - 1)
            val = val:match("^%s*(.-)%s*$")
            table.insert(campos, val)
            c = fin + 1
        end
    end
    return campos
end

-- Determina la nota curvada según Sauro y Lewis (2016)
function sus.obtener_nota(puntuacion)
    if puntuacion >= 84.1 then return "A+"
    elseif puntuacion >= 80.8 then return "A"
    elseif puntuacion >= 78.9 then return "A-"
    elseif puntuacion >= 77.2 then return "B+"
    elseif puntuacion >= 74.1 then return "B"
    elseif puntuacion >= 72.6 then return "B-"
    elseif puntuacion >= 71.1 then return "C+"
    elseif puntuacion >= 65.0 then return "C"
    elseif puntuacion >= 62.7 then return "C-"
    elseif puntuacion >= 51.7 then return "D"
    else return "F" end
end

-- Determina el adjetivo según Bangor, Kortum y Miller (2009)
function sus.obtener_adjetivo(puntuacion)
    if puntuacion >= 88.2 then return "El mejor imaginable"
    elseif puntuacion >= 78.45 then return "Excelente"
    elseif puntuacion >= 61.15 then return "Bueno"
    elseif puntuacion >= 43.3 then return "OK"
    elseif puntuacion >= 28.0 then return "Pobre"
    elseif puntuacion >= 16.4 then return "Horrible"
    else return "El peor imaginable" end
end

-- Determina el rango de aceptabilidad según Bangor, Kortum y Miller (2008)
function sus.obtener_aceptabilidad(puntuacion)
    if puntuacion >= 70.0 then
        return "Aceptable"
    elseif puntuacion >= 50.0 then
        return "Marginal"
    else
        return "No aceptable"
    end
end

-- Exporta resultados a resultados.json según formato especificado (sin redondear)
function sus.exportar_json()
    local archivo, err = io.open("resultados.json", "w")
    if not archivo then
        return
    end
    
    archivo:write("{\n  \"participantes\": [\n")
    for i, reg in ipairs(sus.datos) do
        local coma = (i < #sus.datos) and "," or ""
        archivo:write(string.format(
            '    {"id": "%s", "puntuacion": %.6f, "nota": "%s",\n     "adjetivo": "%s", "aceptabilidad": "%s"}%s\n',
            reg.id, reg.puntuacion, reg.nota, reg.adjetivo, reg.aceptabilidad, coma
        ))
    end
    archivo:write("  ],\n  \"estadisticas\": ")
    archivo:write(string.format(
        '{"n": %d, "media": %.6f, "desviacion": %.6f,\n                   "minimo": %.6f, "maximo": %.6f}\n',
        sus.stats.n, sus.stats.media, sus.stats.desviacion, sus.stats.minimo, sus.stats.maximo
    ))
    archivo:write("}\n")
    archivo:close()
end

-- Carga y procesa el archivo CSV
function sus.cargar_csv(ruta)
    sus.datos = {}
    sus.errores = {}
    local archivo, err = io.open(ruta, "r")
    if not archivo then
        table.insert(sus.errores, "No se pudo abrir el archivo CSV: " .. tostring(err))
        return false
    end

    local linea_num = 0
    local cabecera_leida = false

    for linea in archivo:lines() do
        linea_num = linea_num + 1
        if linea:match("%S") then
            if not cabecera_leida then
                cabecera_leida = true
            else
                local campos = parse_csv_line(linea)
                if #campos < 12 then
                    table.insert(sus.errores, string.format("Línea %d: se esperaban al menos 12 columnas.", linea_num))
                else
                    local id = campos[1]
                    local perfil = campos[2]
                    local respuestas = {}
                    local linea_valida = true

                    for i = 1, 10 do
                        local val = tonumber(campos[2 + i])
                        if not val or val < 1 or val > 5 or math.floor(val) ~= val then
                            table.insert(sus.errores, string.format("Línea %d (usuario '%s'): pregunta q%d inválida.", linea_num, id, i))
                            linea_valida = false
                        else
                            respuestas[i] = val
                        end
                    end

                    local comentario = campos[13] or ""

                    if linea_valida then
                        local suma_contrib = 0
                        local contribuciones = {}
                        for i = 1, 10 do
                            local contrib = 0
                            if i % 2 == 1 then
                                contrib = respuestas[i] - 1
                            else
                                contrib = 5 - respuestas[i]
                            end
                            contribuciones[i] = contrib
                            suma_contrib = suma_contrib + contrib
                        end
                        local puntuacion = suma_contrib * 2.5

                        table.insert(sus.datos, {
                            id = id,
                            perfil = perfil,
                            respuestas = respuestas,
                            contribuciones = contribuciones,
                            suma_contrib = suma_contrib,
                            puntuacion = puntuacion,
                            nota = sus.obtener_nota(puntuacion),
                            adjetivo = sus.obtener_adjetivo(puntuacion),
                            aceptabilidad = sus.obtener_aceptabilidad(puntuacion),
                            comentario = comentario
                        })
                    end
                end
            end
        end
    end
    archivo:close()

    if #sus.datos == 0 then
        table.insert(sus.errores, "El archivo CSV no contiene registros válidos.")
        return false
    end

    local suma = 0
    local min_val = 100
    local max_val = 0

    for _, reg in ipairs(sus.datos) do
        local p = reg.puntuacion
        suma = suma + p
        if p < min_val then min_val = p end
        if p > max_val then max_val = p end
    end

    local n = #sus.datos
    local media = suma / n

    local varianza = 0
    if n > 1 then
        local suma_cuad = 0
        for _, reg in ipairs(sus.datos) do
            suma_cuad = suma_cuad + (reg.puntuacion - media) ^ 2
        end
        varianza = suma_cuad / (n - 1)
    end
    local desviacion = math.sqrt(varianza)

    sus.stats = {
        n = n,
        media = media,
        desviacion = desviacion,
        minimo = min_val,
        maximo = max_val,
        nota_media = sus.obtener_nota(media),
        adjetivo_media = sus.obtener_adjetivo(media),
        aceptabilidad_media = sus.obtener_aceptabilidad(media)
    }

    sus.exportar_json()
    return true
end

-- ============================================================================
-- Definición segura de macros LaTeX (evita código Lua directo en los .tex)
-- ============================================================================
function sus.definir_macros()
    local s = sus.stats
    local d = sus.datos
    
    tex.sprint("\\def\\susN{" .. tostring(s.n or 0) .. "}")
    tex.sprint("\\def\\susMedia{" .. sus.formato_decimal(s.media, 1) .. "}")
    tex.sprint("\\def\\susDesviacion{" .. sus.formato_decimal(s.desviacion, 2) .. "}")
    tex.sprint("\\def\\susMinimo{" .. sus.formato_decimal(s.minimo, 1) .. "}")
    tex.sprint("\\def\\susMaximo{" .. sus.formato_decimal(s.maximo, 1) .. "}")
    tex.sprint("\\def\\susNotaMedia{" .. sus.escapar_latex(s.nota_media) .. "}")
    tex.sprint("\\def\\susAdjetivoMedia{" .. sus.escapar_latex(s.adjetivo_media) .. "}")
    tex.sprint("\\def\\susAceptabilidadMedia{" .. sus.escapar_latex(s.aceptabilidad_media) .. "}")
    
    local m = s.media or 0
    local color_donut = "susRojo"
    if m >= 70 then color_donut = "susVerde"
    elseif m >= 50 then color_donut = "susAmarillo" end
    tex.sprint("\\def\\susColorMedia{" .. color_donut .. "}")

    tex.sprint("\\def\\susMediaRaw{" .. string.format("%.2f", s.media or 0) .. "}")
    tex.sprint("\\def\\susMinimoRaw{" .. string.format("%.2f", s.minimo or 0) .. "}")
    tex.sprint("\\def\\susMaximoRaw{" .. string.format("%.2f", s.maximo or 0) .. "}")

    if #d > 0 then
        local p = d[1]
        tex.sprint("\\def\\susEjId{" .. sus.escapar_latex(p.id) .. "}")
        tex.sprint("\\def\\susEjPerfil{" .. sus.escapar_latex(p.perfil) .. "}")
        tex.sprint("\\def\\susEjPuntuacion{" .. sus.formato_decimal(p.puntuacion, 1) .. "}")
        tex.sprint("\\def\\susEjNota{" .. sus.escapar_latex(p.nota) .. "}")
        tex.sprint("\\def\\susEjAdjetivo{" .. sus.escapar_latex(p.adjetivo) .. "}")
        tex.sprint("\\def\\susEjAceptabilidad{" .. sus.escapar_latex(p.aceptabilidad) .. "}")
        
        tex.sprint("\\def\\susPrimerId{" .. sus.escapar_latex(d[1].id) .. "}")
        tex.sprint("\\def\\susUltimoId{" .. sus.escapar_latex(d[#d].id) .. "}")
    end
end

-- ============================================================================
-- Funciones expuestas a LaTeX mediante tex.print / tex.sprint
-- ============================================================================

function sus.imprimir_errores()
    if #sus.errores > 0 then
        tex.print("\\begin{tcolorbox}[colback=red!10!white,colframe=red!75!black,title={Errores detectados en respuestas.csv}]\\begin{itemize}")
        for _, err in ipairs(sus.errores) do
            tex.print("\\item " .. sus.escapar_latex(err))
        end
        tex.print("\\end{itemize}\\end{tcolorbox}")
    end
end

function sus.imprimir_tabla_perfiles()
    for _, reg in ipairs(sus.datos) do
        local id_tex = sus.escapar_latex(reg.id)
        local perfil_tex = sus.escapar_latex(reg.perfil)
        local comentario_tex = reg.comentario
        if comentario_tex == "" then 
            comentario_tex = "---" 
        else 
            comentario_tex = sus.escapar_latex(comentario_tex) 
        end
        local fila = string.format("%s & %s & %s \\\\ \\hline", id_tex, perfil_tex, comentario_tex)
        tex.print(fila)
    end
end

function sus.imprimir_tabla_resultados()
    for _, reg in ipairs(sus.datos) do
        local r = reg.respuestas
        local fila = string.format("%s & %d & %d & %d & %d & %d & %d & %d & %d & %d & %d & %s & %s & %s & %s \\\\",
            sus.escapar_latex(reg.id),
            r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10],
            sus.formato_decimal(reg.puntuacion, 1),
            sus.escapar_latex(reg.nota),
            sus.escapar_latex(reg.adjetivo),
            sus.escapar_latex(reg.aceptabilidad)
        )
        tex.print(fila)
    end
end

function sus.imprimir_ejemplo_primer_participante()
    if #sus.datos == 0 then
        tex.print("No hay datos disponibles para el ejemplo.")
        return
    end
    local p = sus.datos[1]
    
    tex.print(string.format("A modo de demostración, se detalla el cálculo para el participante \\textbf{%s} (%s):", sus.escapar_latex(p.id), sus.escapar_latex(p.perfil)))
    tex.print("\\begin{itemize}")
    tex.print(string.format("  \\item \\textbf{Respuestas brutas}: $q_1=%d,\\; q_2=%d,\\; q_3=%d,\\; q_4=%d,\\; q_5=%d,\\; q_6=%d,\\; q_7=%d,\\; q_8=%d,\\; q_9=%d,\\; q_{10}=%d$.",
        p.respuestas[1], p.respuestas[2], p.respuestas[3], p.respuestas[4], p.respuestas[5],
        p.respuestas[6], p.respuestas[7], p.respuestas[8], p.respuestas[9], p.respuestas[10]))
    tex.print(string.format("  \\item \\textbf{Contribuciones de ítems impares} ($q_i - 1$): " ..
        "$c_1 = %d - 1 = %d$,\\quad $c_3 = %d - 1 = %d$,\\quad $c_5 = %d - 1 = %d$,\\quad $c_7 = %d - 1 = %d$,\\quad $c_9 = %d - 1 = %d$.",
        p.respuestas[1], p.contribuciones[1], p.respuestas[3], p.contribuciones[3],
        p.respuestas[5], p.contribuciones[5], p.respuestas[7], p.contribuciones[7],
        p.respuestas[9], p.contribuciones[9]))
    tex.print(string.format("  \\item \\textbf{Contribuciones de ítems pares} ($5 - q_i$): " ..
        "$c_2 = 5 - %d = %d$,\\quad $c_4 = 5 - %d = %d$,\\quad $c_6 = 5 - %d = %d$,\\quad $c_8 = 5 - %d = %d$,\\quad $c_{10} = 5 - %d = %d$.",
        p.respuestas[2], p.contribuciones[2], p.respuestas[4], p.contribuciones[4],
        p.respuestas[6], p.contribuciones[6], p.respuestas[8], p.contribuciones[8],
        p.respuestas[10], p.contribuciones[10]))
    tex.print(string.format("  \\item \\textbf{Suma de contribuciones}: " ..
        "\\[ \\sum_{i=1}^{10} c_i = %d + %d + %d + %d + %d + %d + %d + %d + %d + %d = %d \\]",
        p.contribuciones[1], p.contribuciones[2], p.contribuciones[3], p.contribuciones[4], p.contribuciones[5],
        p.contribuciones[6], p.contribuciones[7], p.contribuciones[8], p.contribuciones[9], p.contribuciones[10],
        p.suma_contrib))
    tex.print(string.format("  \\item \\textbf{Puntuación SUS final}: " ..
        "\\[ \\text{SUS} = %d \\times 2{,}5 = \\mathbf{%s} \\]",
        p.suma_contrib, sus.formato_decimal(p.puntuacion, 1)))
    tex.print(string.format("\\end{itemize} Esta puntuación de %s equivale a una calificación \\textbf{%s}, adjetivo \\textbf{%s} y aceptabilidad \\textbf{%s}.",
        sus.formato_decimal(p.puntuacion, 1), sus.escapar_latex(p.nota), sus.escapar_latex(p.adjetivo), sus.escapar_latex(p.aceptabilidad)))
end

function sus.imprimir_coordenadas_barras()
    for _, reg in ipairs(sus.datos) do
        tex.sprint(string.format("(%s, %.2f) ", sus.escapar_latex(reg.id), reg.puntuacion))
    end
end

function sus.imprimir_etiquetas_barras()
    local lista = {}
    for _, reg in ipairs(sus.datos) do
        table.insert(lista, sus.escapar_latex(reg.id))
    end
    tex.sprint(table.concat(lista, ", "))
end

-- ============================================================================
-- Interpretación dinámica de resultados según datos (con tex.print para seguridad)
-- ============================================================================

function sus.imprimir_conclusion()
    local s = sus.stats
    local media = s.media or 0

    if media >= 68 then
        tex.print("Al situarse por encima del umbral normativo estándar de 68 puntos, la usabilidad global del sistema se considera superior a la media de la industria. ")
    else
        tex.print("Al situarse por debajo de la media estándar de referencia de 68 puntos, los resultados indican la existencia de barreras de uso relevantes en el sistema evaluado. ")
    end

    if s.aceptabilidad_media == "Aceptable" then
        tex.print("La calificación de aceptabilidad \\textbf{Aceptable} confirma que los usuarios logran completar los flujos habituales sin fricción crítica, cumpliendo satisfactoriamente los criterios funcionales requeridos. ")
    elseif s.aceptabilidad_media == "Marginal" then
        tex.print("La calificación de aceptabilidad \\textbf{Marginal} advierte de que, si bien la interacción es viable, se precisan ajustes de diseño prioritarios y optimización de flujos antes de su despliegue definitivo. ")
    else
        tex.print("La clasificación de \\textbf{No aceptable} señala que el sistema impone dificultades sustanciales que comprometen la adopción del producto y demandan un rediseño en profundidad. ")
    end

    tex.print("\\medskip")
    tex.print("\\noindent\\textbf{Análisis cualitativo del evaluador:}")
    tex.print("\\begin{itemize}")
    tex.print("  \\item \\textbf{Puntos fuertes destacados}: \\textcolor{red}{[Completar: aspectos positivos y tareas ejecutadas con mayor agilidad]}.")
    tex.print("  \\item \\textbf{Principales dificultades detectadas}: \\textcolor{red}{[Completar: tareas con más problemas o dudas manifestadas]}.")
    tex.print("  \\item \\textbf{Acciones de mejora propuestas}: \\textcolor{red}{[Completar: cambios de interfaz, retroalimentación o simplificación de flujos]}.")
    tex.print("\\end{itemize}")
end

-- ============================================================================
-- Conclusiones dinámicas para la defensa Beamer
-- ============================================================================

function sus.imprimir_conclusiones_defensa()
    local s = sus.stats
    local media = s.media or 0
    local acept = s.aceptabilidad_media or "Desconocida"

    tex.print("\\begin{block}{Conclusiones de la Evaluación SUS}")
    tex.print("\\begin{itemize}")
    
    if media >= 68 then
        tex.print(string.format("  \\item La media muestral de \\textbf{%.1f} se sitúa por encima del valor estándar de referencia industrial (68 puntos).", media))
    else
        tex.print(string.format("  \\item La media muestral de \\textbf{%.1f} se sitúa por debajo del valor estándar de referencia industrial (68 puntos).", media))
    end
    
    if acept == "Aceptable" then
        tex.print("  \\item La aceptabilidad global es \\textbf{Aceptable}, indicando que los usuarios completan los flujos de interacción satisfactoriamente.")
    elseif acept == "Marginal" then
        tex.print("  \\item La aceptabilidad global es \\textbf{Marginal}, reflejando deficiencias de usabilidad que requieren corrección.")
    else
        tex.print("  \\item La aceptabilidad global es \\textbf{No aceptable}, evidenciando barreras severas en la operabilidad del sistema.")
    end
    
    tex.print("  \\item \\textbf{Calificación obtenida}: nota " .. sus.escapar_latex(s.nota_media) .. " con adjetivo \\enquote{" .. sus.escapar_latex(s.adjetivo_media) .. "}.")
    tex.print("\\end{itemize}")
    tex.print("\\end{block}")
end

return sus
