function home(event){
    event.preventDefault();
    const containerMain = document.getElementById("id-container-main");

    containerMain.innerHTML =

    `
             <div class="container-infor-main">
        <div>
            <h1>Informaçoes gerais</h1>
        </div>
        <div class="container-infor-data-user">
            <div class="container-infor-user-home">
                <h2>Dados do Inquilino</h2>
                <h5>Nome Completo</h5>
                <p>Fulano da silva</p>
                <h5>Cadastro de Pessoa Fisica</h5>
                <p>000.000.000-00</p>
                <h5>Idade</h5>
                <p>29 anos</p>
            </div>
        <div class="container-infor-user-home">
                <h2>Dados do Apartamento</h2>
                <h5>Número do anda</h5>
                <p>N 4</p>
                <h5>Número da casa</h5>
                <p>N 5</p>
                <h5>Quantidade de moradores</h5>
                <p>4</p>

            </div>
    </div>

    `;
}

function spaceLaser(event){
    event.preventDefault()

    var date = new Date();
    var day = String(date.getDate()).padStart(2,'0')
    var month = String(date.getMonth()+1).padStart(2,'0')
    var year = date.getFullYear();

    var todayDate = `${year}-${month}-${day}`

    console.log(day, month, year)

    const containerMain = document.getElementById("id-container-main");

    containerMain.innerHTML =`
    <div>
        <h1>Espaço de lazer</h1>
    </div>
    <div class="main-form-laisure">
    <form>
       <div class="mb-3">
            <label for="exampleFormControlInput1" class="form-label"><p>Data</p></label>
            <input type="date" class="form-control form-control-lg" id="exampleFormControlInput1" placeholder="" min="${todayDate}">
        </div>
        <div class="mb-3">
            <p>Espaços</p> 
            <input class="" type="checkbox" id="space" name="espace1" value="Bike">
            <label for="space1">Piscina</label><br>
            <input type="checkbox" id="space2" name="espace2" value="Car">
            <label for="space2">Quadra</label><br>
            <input type="checkbox" id="space3" name="espace3" value="Boat">
            <label for="space3">Churrasqueira</label>
        </div>
        <div class="mb-3">
            <label for="exampleFormControlTextarea1" class="form-label"><p>Informações do evento</p></label>
            <textarea class="form-control form-control-lg" id="exampleFormControlTextarea1" rows="3"></textarea>
        </div>
        <button type="button" class="btn btn-primary">Envia solicitação</button>
        </form>
        <div>
         <strong><p>Resultado da sua requisição chegará via e-mail cadastrado!</p></strong>   
        </div>
    </div>
    `

}

function parking(event){
    event.preventDefault();

    const containerMain = document.getElementById("id-container-main");

    containerMain.innerHTML = `
    
    <h1>Teste</h1>
    
    `

}