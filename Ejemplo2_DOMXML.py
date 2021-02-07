from xml.dom import minidom
doc = minidom.parse("Ejemplo2_DOMXML.xml")

estudiantes = doc.getElementsByTagName("estudiante")
for estudiante in estudiantes:
    sid = estudiante.getAttribute("id")
    nombre = estudiante.getElementsByTagName("nombre")[0]
    username = estudiante.getElementsByTagName("username")[0]
    password = estudiante.getElementsByTagName("password")[0]
    
    print("id:%s " % sid)
    print("nombre:%s" % nombre.firstChild.data)
    print("username:%s" % username.firstChild.data)
    print("password:%s" % password.firstChild.data)