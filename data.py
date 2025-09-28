# data.py

def get_crime_data():
    """
    Esta función contiene todos los datos de los casos en una lista de diccionarios.
    Es un método mucho más robusto que un archivo CSV.
    """
    casos = [
        {
            "id": 1,
            "nombre": "El celador de Olot",
            "resumen_corto": "Joan Vila, un auxiliar de geriatría en La Caritat de Olot, confesó haber asesinado a 11 ancianos entre 2009 y 2010.",
            "cronica_detallada": "Conocido como 'El Ángel de la Muerte', Joan Vila Dilmé trabajaba en el geriátrico La Caritat. Durante meses, administró cócteles de fármacos o productos cáusticos a los residentes, causando su muerte. Inicialmente, sus crímenes pasaron desapercibidos, atribuidos a la avanzada edad de las víctimas. Fue la muerte de una residente, Paquita Gironès, con indicios extraños, la que destapó el horror. Vila confesó los crímenes alegando que lo hacía 'para evitarles el sufrimiento', una versión que los psicólogos desmontaron, revelando un perfil de asesino metódico con una profunda necesidad de control y protagonismo.",
            "fecha_suceso": 2010,
            "ubicacion_principal": "Geriátrico La Caritat, Olot",
            "lat": 42.176944,
            "lon": 2.485556,
            "provincia": "Girona",
            "status": "Resuelto",
            "tags": "Asesino en serie, Urbano",
            "foto_url_archivo": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.elperiodico.com%2Fes%2Fextra%2F20221126%2Fcelador-olot-joan-vila-asesino-serie-carceles-catalanas-78810330&psig=AOvVaw21Gj_Fq-lUjLd2s0Q5Yx5d&ust=1727600889241000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCNi-gJ3h04MDFQAAAAAdAAAAABAE"
        },
        {
            "id": 2,
            "nombre": "El crimen de la Guardia Urbana",
            "resumen_corto": "El cuerpo calcinado del agente Pedro R. aparece en el pantano de Foix, destapando un triángulo amoroso mortal.",
            "cronica_detallada": "El caso, que conmocionó a la opinión pública, reveló una red de relaciones tóxicas, engaños y violencia dentro del cuerpo policial de Barcelona. Rosa Peral, Pedro R. y Albert López formaban un triángulo amoroso que culminó con el asesinato de Pedro. Las pruebas demostraron que Rosa y Albert planificaron y ejecutaron el crimen en la casa que ella compartía con la víctima. El juicio fue uno de los más mediáticos de los últimos años, con acusaciones cruzadas entre los dos amantes, quienes finalmente fueron condenados por asesinato.",
            "fecha_suceso": 2017,
            "ubicacion_principal": "Pantano de Foix, Castellet i la Gornal",
            "lat": 41.258,
            "lon": 1.61,
            "provincia": "Barcelona",
            "status": "Resuelto",
            "tags": "Pasional, Policial",
            "foto_url_archivo": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.lavanguardia.com%2Fpeliculas-series%2Fpersonas%2Frosa-peral-1845199&psig=AOvVaw0_1uQoB3Z8f4R5d9E6r7rJ&ust=1727600936384000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCJDftbDn04MDFQAAAAAdAAAAABAE"
        },
        {
            "id": 3,
            "nombre": "El asesinato de Helena Jubany",
            "resumen_corto": "En 2001, el cuerpo de la bibliotecaria Helena Jubany fue encontrado en un patio de Sabadell. El caso sigue sin resolverse.",
            "cronica_detallada": "Helena fue arrojada inconsciente, pero aún con vida, desde la azotea de un edificio. La investigación se centró en su círculo de amigos de la Unió Excursionista de Sabadell. Una amiga, Montse Careta, fue detenida como principal sospechosa y se suicidó en prisión preventiva, defendiendo siempre su inocencia. Las pruebas caligráficas de los anónimos que Helena recibió días antes, que eran la clave del caso, han sido objeto de controversia durante años. A día de hoy, la familia de Helena sigue luchando por reabrir el caso, convirtiéndolo en un símbolo de la justicia pendiente en Cataluña.",
            "fecha_suceso": 2001,
            "ubicacion_principal": "C/ Calvet d'Estrella 48, Sabadell",
            "lat": 41.5458,
            "lon": 2.106,
            "provincia": "Barcelona",
            "status": "Sin resolver",
            "tags": "Misterio, Urbano",
            "foto_url_archivo": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.ccma.cat%2F324%2Fqui-va-matar-helena-jubany-les-claus-dun-crim-sense-resoldre-20-anys-despres%2Fnoticia%2F3135323%2F&psig=AOvVaw314Rj_bJ8f1d8m9s6w1x8x&ust=1727601007797000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCLjG38nn04MDFQAAAAAdAAAAABAE"
        },
        {
            "id": 4,
            "nombre": "La Vampira del Raval",
            "resumen_corto": "Enriqueta Martí, una mujer de la Barcelona de 1912, fue acusada de secuestrar y asesinar niños para crear pócimas.",
            "cronica_detallada": "La crónica negra cuenta que Enriqueta raptaba niños para extraerles la sangre, las grasas y la médula ósea, con las que elaboraba pócimas que vendía a la burguesía. Fue detenida en su piso de la calle Ponent (hoy Joaquim Costa) donde encontraron a dos niñas. Aunque la prensa la pintó como un monstruo, investigaciones posteriores sugieren que la parte de los asesinatos en serie y la brujería pudo ser una exageración para ocultar una red de pederastia que salpicaba a las clases altas. Murió en prisión antes de ser juzgada.",
            "fecha_suceso": 1912,
            "ubicacion_principal": "C/ Joaquim Costa 29, Barcelona",
            "lat": 41.3828,
            "lon": -2.1687,
            "provincia": "Barcelona",
            "status": "Resuelto",
            "tags": "Histórico, Asesino en serie",
            "foto_url_archivo": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.lavanguardia.com%2Flocal%2Fbarcelona%2F20220310%2F8110549%2Fenriqueta-marti-vampira-raval-realidad-mito.html&psig=AOvVaw2j_2yPjJ5b1k_G2g_3f8eZ&ust=1727601053427000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCKjM59rn04MDFQAAAAAdAAAAABAE"
        },
        {
            "id": 5,
            "nombre": "El crimen de Tor",
            "resumen_corto": "La disputa por la propiedad de la montaña de Tor culminó en 1995 con el asesinato de Josep Montané, 'Sansa'.",
            "cronica_detallada": "Tor es un enclave de alta montaña cuya propiedad se convirtió en una guerra de intereses y contrabando. 'Sansa' intentó establecer una sociedad de propietarios, pero se encontró con una feroz oposición. Fue asesinado a tiros en su casa. Las sospechas recayeron sobre muchos, desde contrabandistas a vecinos rivales. Dos de ellos, Lázaro y 'El Palanca', fueron los principales acusados, pero finalmente absueltos por falta de pruebas. El crimen de Tor, popularizado por Carles Porta, es el epítome del 'true crime' rural, un western moderno en pleno Pirineo que sigue oficialmente sin culpable.",
            "fecha_suceso": 1995,
            "ubicacion_principal": "Tor, Alins",
            "lat": 42.593,
            "lon": 1.402,
            "provincia": "Lleida",
            "status": "Sin resolver",
            "tags": "Rural, Misterio",
            "foto_url_archivo": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.viajar.elperiodico.com%2Fdestinos%2Festas-son-casas-tor-pueblo-maldito-pirineos-donde-aun-vive-gente&psig=AOvVaw19lB9yJ7R9d_h6Q8f7w8A4&ust=1727601091599000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCJjY9N3n04MDFQAAAAAdAAAAABAE"
        }
    ]
    return casos