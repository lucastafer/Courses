var http = require("http")

http.createServer(function(req, res) {
    res.end("<h1>Bem vindo!</h1><br><h4>Guia do Programador.</h4>")
}).listen(8181)
console.log("Meu servidor está rodando!")
