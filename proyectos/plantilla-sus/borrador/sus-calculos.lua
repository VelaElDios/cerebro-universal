-- ============================================================================
-- sus-calculos.lua
-- Motor de procesamiento de datos SUS (System Usability Scale) para LuaLaTeX
-- ============================================================================

local sus = {}
sus.datos = {}
sus.stats = {}
sus.errores = {}

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
    local pattern = '([^",]+)|"([^"]*)"'
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
            c = fin + 2 -- salta comilla de cierre y posible coma
        else
            local fin = line:find(',', c)
            if not fin then fin = longitud + 1 end
            local val = line:sub(c, fin - 1)
            -- Trim espacios blancos en los extremos
            val = val:match("^%s*(.-)%s*$")
            table.insert(campos, val)
            c = fin + 1
        end
    end
    return campos
end

-- Determina la nota curvada según Sauro y Lewis (2016)
-- TODO: Revisor, comprobar correspondencia de percentiles y rangos según Sauro & Lewis (2016)
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

-- Determina el adjetivo descriptivo según Bangor, Kortum y Miller (2009)
-- TODO: Revisor, comprobar umbrales exactos de los 7 adjetivos de Bangor et al. (2009)
function sus.obtener_adjetivo(puntuacion)
    if puntuacion >= 85.5 then return "El mejor imaginable"
    elseif puntuacion >= 72.6 then return "Excelente"
    elseif puntuacion >= 62.7 then return "Bueno"
    elseif puntuacion >= 51.7 then return "Regular (OK)"
    elseif puntuacion >= 35.7 then return "Pobre"
    elseif puntuacion >= 20.5 then return "Malo"
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
        -- Ignorar líneas vacías
        if linea:match("%S") then
            if not cabecera_leida then
                cabecera_leida = true
            else
                local campos = parse_csv_line(linea)
                if #campos < 12 then
                    table.insert(sus.errores, string.format("Línea %d: se esperaban al menos 12 columnas (id, perfil, q1..q10), encontradas %d.", linea_num, #campos))
                else
                    local id = campos[1]
                    local perfil = campos[2]
                    local respuestas = {}
                    local linea_valida = true

                    for i = 1, 10 do
                        local val = tonumber(campos[2 + i])
                        if not val or val < 1 or val > 5 or math.floor(val) ~= val then
                            table.insert(sus.errores, string.format("Línea %d (usuario '%s'): pregunta q%d tiene un valor inválido ('%s'). Debe ser un entero entre 1 y 5.", linea_num, id, i, tostring(campos[2 + i])))
                            linea_valida = false
                        else
                            respuestas[i] = val
                        end
                    end

                    local comentario = campos[13] or ""

                    if linea_valida then
                        -- Cálculo de aportaciones SUS
                        -- Ítems impares: respuesta - 1
                        -- Ítems pares: 5 - respuesta
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

    -- Cálculo de estadísticas globales
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

    -- Desviación típica muestral (dividida por n - 1 si n > 1)
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

    return true
end

-- ============================================================================
-- Funciones expuestas a LaTeX mediante tex.sprint
-- ============================================================================

-- Comprueba si hay errores y genera un aviso visible
function sus.imprimir_errores()
    if #sus.errores > 0 then
        local txt = "\\begin{tcolorbox}[colback=red!10!white,colframe=red!75!black,title={Errores detectados en respuestas.csv}]\\begin{itemize}"
        for _, err in ipairs(sus.errores) do
            txt = txt .. "\\item " .. err
        end
        txt = txt .. "\\end{itemize}\\end{tcolorbox}"
        tex.sprint(txt)
    end
end

-- Devolver un valor escalar estadístico
function sus.get_stat(campo, decimales)
    if not sus.stats[campo] then
        tex.sprint("---")
        return
    end
    local val = sus.stats[campo]
    if type(val) == "number" then
        tex.sprint(sus.formato_decimal(val, decimales or 1))
    else
        tex.sprint(tostring(val))
    end
end

-- Devolver un valor numérico crudo con punto decimal para TikZ
function sus.get_stat_raw(campo)
    local val = sus.stats[campo] or 0
    tex.sprint(string.format("%.2f", val))
end

-- Imprime la tabla de perfiles de participantes
function sus.imprimir_tabla_perfiles()
    for _, reg in ipairs(sus.datos) do
        local id_tex = reg.id
        local perfil_tex = reg.perfil
        local comentario_tex = reg.comentario
        if comentario_tex == "" then comentario_tex = "---" end
        local fila = string.format("%s & %s & %s \\\\ \\hline", id_tex, perfil_tex, comentario_tex)
        tex.sprint(fila)
    end
end

-- Imprime la tabla completa de resultados con las 10 respuestas individuales
function sus.imprimir_tabla_resultados()
    for _, reg in ipairs(sus.datos) do
        local r = reg.respuestas
        local fila = string.format("%s & %d & %d & %d & %d & %d & %d & %d & %d & %d & %d & %s & %s & %s & %s \\\\",
            reg.id,
            r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10],
            sus.formato_decimal(reg.puntuacion, 1),
            reg.nota,
            reg.adjetivo,
            reg.aceptabilidad
        )
        tex.sprint(fila)
    end
end

-- Imprime el desglose paso a paso del primer participante para el ejemplo de cálculo
function sus.imprimir_ejemplo_primer_participante()
    if #sus.datos == 0 then
        tex.sprint("No hay datos disponibles para el ejemplo.")
        return
    end
    local p = sus.datos[1]
    local texto = string.format(
        "A modo de demostración, se detalla el cálculo para el participante \\textbf{%s} (%s):\n\n" ..
        "\\begin{itemize}\n" ..
        "  \\item \\textbf{Respuestas brutas}: $q_1=%d,\\; q_2=%d,\\; q_3=%d,\\; q_4=%d,\\; q_5=%d,\\; q_6=%d,\\; q_7=%d,\\; q_8=%d,\\; q_9=%d,\\; q_{10}=%d$.\n" ..
        "  \\item \\textbf{Contribuciones de ítems impares} ($q_i - 1$):\n" ..
        "    $c_1 = %d - 1 = %d$,\\quad $c_3 = %d - 1 = %d$,\\quad $c_5 = %d - 1 = %d$,\\quad $c_7 = %d - 1 = %d$,\\quad $c_9 = %d - 1 = %d$.\n" ..
        "  \\item \\textbf{Contribuciones de ítems pares} ($5 - q_i$):\n" ..
        "    $c_2 = 5 - %d = %d$,\\quad $c_4 = 5 - %d = %d$,\\quad $c_6 = 5 - %d = %d$,\\quad $c_8 = 5 - %d = %d$,\\quad $c_{10} = 5 - %d = %d$.\n" ..
        "  \\item \\textbf{Suma de contribuciones}:\n" ..
        "    \\[ \\sum_{i=1}^{10} c_i = %d + %d + %d + %d + %d + %d + %d + %d + %d + %d = %d \\]\n" ..
        "  \\item \\textbf{Puntuación SUS final}:\n" ..
        "    \\[ \\text{SUS} = %d \\times 2{,}5 = \\mathbf{%s} \\]\n" ..
        "\\end{itemize}\n" ..
        "Esta puntuación de %s equivale a una calificación \\textbf{%s}, adjetivo \\textbf{%s} y aceptabilidad \\textbf{%s}.",
        p.id, p.perfil,
        p.respuestas[1], p.respuestas[2], p.respuestas[3], p.respuestas[4], p.respuestas[5],
        p.respuestas[6], p.respuestas[7], p.respuestas[8], p.respuestas[9], p.respuestas[10],
        p.respuestas[1], p.contribuciones[1],
        p.respuestas[3], p.contribuciones[3],
        p.respuestas[5], p.contribuciones[5],
        p.respuestas[7], p.contribuciones[7],
        p.respuestas[9], p.contribuciones[9],
        p.respuestas[2], p.contribuciones[2],
        p.respuestas[4], p.contribuciones[4],
        p.respuestas[6], p.contribuciones[6],
        p.respuestas[8], p.contribuciones[8],
        p.respuestas[10], p.contribuciones[10],
        p.contribuciones[1], p.contribuciones[2], p.contribuciones[3], p.contribuciones[4], p.contribuciones[5],
        p.contribuciones[6], p.contribuciones[7], p.contribuciones[8], p.contribuciones[9], p.contribuciones[10],
        p.suma_contrib,
        p.suma_contrib,
        sus.formato_decimal(p.puntuacion, 1),
        sus.formato_decimal(p.puntuacion, 1),
        p.nota,
        p.adjetivo,
        p.aceptabilidad
    )
    tex.sprint(texto)
end

-- Exporta coordenadas de las barras individuales para pgfplots/TikZ
function sus.imprimir_coordenadas_barras()
    for i, reg in ipairs(sus.datos) do
        -- Formato: (id, puntuacion)
        tex.sprint(string.format("(%s, %.2f) ", reg.id, reg.puntuacion))
    end
end

-- Exporta etiquetas de participantes para el eje simbólico de pgfplots
function sus.imprimir_etiquetas_barras()
    local lista = {}
    for _, reg in ipairs(sus.datos) do
        table.insert(lista, reg.id)
    end
    tex.sprint(table.concat(lista, ", "))
end

return sus
