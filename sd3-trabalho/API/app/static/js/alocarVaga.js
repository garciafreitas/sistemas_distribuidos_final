function vagaAlocada(){
    preventDefault()
    url = "http://192.168.3.143:5000/estacionamento"

    vaga = document.getElementById("vaga").value.replace(/\D/g,'');
    modelo = document.getElementById("modelo").value.replace(/\D/g,'');
    placa = document.getElementById("placa").value.replace(/\D/g,'');

    var request = new XMLHttpRequest();
    
    request.open('GET',url);
    request.onerror = function(e){
        document.getElementById('vaga'+'modelo'+'placa').innerHTML = 'Vaga, Modelo e Placa'
    }
    request.onload = () =>{
        var jsondata =JSON.parse(request.responseText);

        if(jsondata.erro === true){
            document.getElementById('vaga'+'modelo'+'placa').innerHTML = 'Vaga, Modelo e Placa Invalidos'
        }
        else
        {
            document.getElementById('vaga'+'modelo'+'placa').innerHTML =
            '<h1>'+'Vaga:'+'</h1>' + jsondata.vaga + '<br>'+
            '<h1>'+'Modelo:'+'</h1>' + jsondata.$modelo + '<br>'+
            '<h1>'+'Placa:'+'</h1>' + jsondata.placa + '<br>';

        }
    }
    request.send();
}