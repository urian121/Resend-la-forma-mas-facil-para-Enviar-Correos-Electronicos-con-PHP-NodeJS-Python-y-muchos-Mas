import express from "express";
import cors from "cors";

/**
 * Para el envío de Email
 */
import { Resend } from "resend";

// Creando una nueva aplicación Express.
const app = express();
const resend = new Resend("re_gQYDfsg9_DY6dVbrbi1yM6nTHSyuSKNkc");

app.use(cors());

app.use(express.json()); // Para analizar JSON en el cuerpo de las solicitudes
app.use(express.urlencoded({ extended: true })); // Para analizar datos de formulario en el cuerpo de las solicitudes

app.use("/public", express.static("public"));

/**
 * Establecer EJS como el Motor de plantillas
 */
app.set("view engine", "ejs");
app.set("views", "./views");

/**
 * Definiendo mi ruta Home
 */
app.get("/", (req, res) => {
  res.render("inicio", {
    rutaActual: "/",
  });
});

app.post("/enviando-email-con-resend-node-express", async (req, res) => {
  console.log(req.body);
  for (const campo in req.body) {
    if (!req.body[campo]) {
      res.send(`Error: El campo ${campo} está vacío.`);
      return;
    }
  }

  /**
   * Desestructuración de los datos del body
   */
  const { nombre_cliente, email_cliente, mensaje_cliente } = req.body;
  try {
    const data = await resend.emails.send({
      from: "NodeJS + Express <nodeExpress@resend.dev>",
      to: ["urian1213viera@gmail.com"],
      subject: "Email desde Node & Express",
      html: `<p>Hola gente, recibiendo email desde Node con Express 😲 🙀 🤯  
        datos del Cliente:</p>
        <p>Cliente: ${nombre_cliente}</p> 
        <p>Cliente: ${email_cliente}</p> 
        <p>Cliente: ${mensaje_cliente}</p> `,
    });

    console.log("Respuesta enviada:", data);

    // Respuesta JSON después de la redirección
    //res.status(200).json({ data });

    // Redirigir antes de enviar la respuesta JSON
    res.render("inicio", {
      rutaActual: "/",
    });
  } catch (error) {
    res.status(500).json({ error });
  }
});

// Iniciar el servidor con Express
const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
  console.log(`Servidor escuchando en http://localhost:${PORT}`);
});
