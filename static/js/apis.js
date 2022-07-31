function clasificadorModelo(modelo, entrada) {
    var headers =  { 'Content-Type': 'application/json'};
    var  data = JSON.stringify({modelo:"rf",dataset:"sintomas", entrada:"tengo fiebre y dolor de cabeza"})
    $.ajax({
        type:"POST", 
        url:"http://localhost:5000/clasificadorModelo",
        data,
        contentType: "application/json",
        dataType: "json", 
        success:function(datos){ 
            console.log(datos)
            for(var i = 0; i < datos.Respuesta.columnas.length; i++)
            {
                var columna = datos.Respuesta.columnas[i];
                var salida = datos.Respuesta.salidaModelo[i]
                
                
                console.log(columna, salida)
            }
         },
    })
  }