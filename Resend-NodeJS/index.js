import { Resend } from "resend";
//const resend = new Resend("Aqui va la key");
const resend = new Resend("");

const sendEmail = async () => {
  try {
    const data = await resend.emails.send({
      from: "NodeJS <node@resend.dev>",
      to: ["urian1213viera@gmail.com"],
      subject: "Email desde NodeJS",
      html: "<p>Hola Comunidad, enviando email desde NodeJS con Resend 🤯",
    });

    console.log(data);
  } catch (error) {
    console.error(error);
  }
};

sendEmail();
