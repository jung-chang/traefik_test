import React, { useState } from "react";

// const SERVER = "http://api.localhost.com";
const SERVER = "https://api.mewslet.com";


console.log(`NODE_ENV: ${process.env.NODE_ENV}, SERVER: ${SERVER}`);

const About = () => {
    const [data, setData] = useState("");

    fetch(`${SERVER}/`, {
        method: "GET",
        mode: "cors",
        headers: {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        }
    }).then(async (response: any) => {
        const data = await response.json();
        console.log(data);
        setData(JSON.stringify(data));
    });

    return <div>Traefik Test: {data}</div>
}

export default About;
