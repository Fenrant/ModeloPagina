

function clasificadorModelo(modelo, dataset) {
    var entrada = document.getElementById("myTextarea").value;
    var  data = JSON.stringify({modelo, dataset, entrada})
    $.ajax({
        type:"POST", 
        url:"http://localhost:5000/clasificadorModelo",
        data,
        contentType: "application/json",
        dataType: "json", 
        success:function(datos){ 
            var sintomas;
            for(var i = 0; i < datos.Respuesta.columnas.length; i++)
            {
                var columna = datos.Respuesta.columnas[i];
                var salida = datos.Respuesta.salidaModelo[i]
                var html = `
                <div class="col-lg-3 col-md-12 col-sm-12 content-column">
                    <div class="project-block-four">
                        <div class="inner-box">
                            <figure class="image-box">
                                <img src="http://localhost:5000/static/images/clasificacionModelo/${columna}.jpg" alt="">
                                <div style="
                                    position: absolute;
                                    left: 20px;
                                    top: 20px;
                                    width: 64px;
                                    border-radius: 50%;
                                    z-index: 1;
                                "><img src="http://localhost:5000/static/images/icons/${salida === 1 ? "success": "error"}.png" alt=""></div>
                            </figure>
                            <div class="text">
                                <h5>${columna.charAt(0).toUpperCase() + columna.toLowerCase().slice(1)}</h5>
                            </div>
                        </div>
                    </div>
                </div>`
                if(i == 0){
                    sintomas = html;
                }else{
                    sintomas +=html
                }
               
            }
            document.getElementById("sintomas").innerHTML = sintomas;
        },
    })
  }