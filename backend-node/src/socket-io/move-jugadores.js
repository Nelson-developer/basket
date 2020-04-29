import SocketIO from "socket.io";


export  function socketMove(servidor) {
    const io = SocketIO.listen(servidor)

    io.on('connection', (socket) =>{
      console.log('nueva conexion', socket.id);
      //recibiendo datos del cliente
       socket.on('mimensaje', (data) =>{
           console.log(data);
           socket.emit('mimensaje:server', data)
       })

       socket.on('tablero', (datos) =>{
        console.log(datos);
        socket.emit('mimensaje:servidor', datos)
    })
   })
 }