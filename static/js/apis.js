(function () {
        document.getElementById("load").style.display = 'none'
})();
function clasificadorModelo(modelo, dataset) {
    var entrada = document.getElementById("myTextarea").value;
    var  data = JSON.stringify({modelo, dataset, entrada})
    document.getElementById("sintomas").style.display = 'none'; 
    document.getElementById("botonVerMas").style.display = 'none'; 
    document.getElementById("load").style.display = ''
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
            document.getElementById("sintomas").style.display = ''; 
            document.getElementById("botonVerMas").style.display = '';
            document.getElementById("sintomas").innerHTML = sintomas;
            
            document.getElementById("botonVerMas").innerHTML = `<div class="row clearfix" style="margin-bottom: 5%; text-align: end; margin-right: 2%">
            <div class="col-lg-12 col-md-12 col-sm-12 content-column">
                <div class="content-box wow fadeInUp animated" data-wow-delay="00ms" data-wow-duration="1500ms">
                    <div class="btn-box">
                        <a href=${dataset == "sintomas"? "/prediccion/rf/sintomas/graficasSintomas": "/prediccion/rf/recomendaciones/graficasRecomendaciones"} class="theme-btn btn-ten">Ver Más</a>
                    </div>
                </div>
            </div>
        </div>`;
        document.getElementById("load").style.display = 'none'; 
        },
        
    })
  }