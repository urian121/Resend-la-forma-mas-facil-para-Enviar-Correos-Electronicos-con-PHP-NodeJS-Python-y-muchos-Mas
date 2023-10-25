import { Resend } from "resend";
const resend = new Resend("re_gQYDfsg9_DY6dVbrbi1yM6nTHSyuSKNkc");

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
