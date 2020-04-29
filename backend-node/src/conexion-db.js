import { connect } from "mongoose";

export async function ConectarDB() {
    try {
       await connect("mongodb://localhost:27017/basket", {
        useNewUrlParser: true,
        useUnifiedTopology: true
       })
       console.log('conectado a MongoDB');
       
    } catch (error) {
        console.log('error al conectarse a la base de datos');
        
    }
}