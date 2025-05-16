const API_URL = "http://TU_IP_O_DOMINIO/api/dato";

async function obtenerDatos() {
    try {
        const res = await fetch(API_URL);
        const data = await res.json();

        document.getElementById("temperatura").textContent = data.temperatura.toFixed(2);
        document.getElementById("ph").textContent = data.ph.toFixed(2);
        document.getElementById("temperaturaSet").value = data.temperaturaSet;
        document.getElementById("phSet").value = data.phSet;
        document.getElementById("tDis").value = data.tDis;
        document.getElementById("vDis").value = data.vDis;

    } catch (err) {
        console.error("Error al obtener datos:", err);
    }
}

// Envía los valores modificados al backend
async function enviarDatos() {
    const payload = {
        temperaturaSet: parseFloat(document.getElementById("temperaturaSet").value),
        phSet: parseFloat(document.getElementById("phSet").value),
        tDis: parseInt(document.getElementById("tDis").value),
        vDis: parseInt(document.getElementById("vDis").value),
    };

    try {
        await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });
    } catch (err) {
        console.error("Error al enviar datos:", err);
    }
}

// Envía el comando "dispensar"
async function enviarDispensar() {
    try {
        await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ dispensar: true })
        });
        alert("Comando 'dispensar' enviado.");
    } catch (err) {
        console.error("Error al enviar dispensar:", err);
    }
}

// Detectar cambios en inputs para enviar datos
["temperaturaSet", "phSet", "tDis", "vDis"].forEach(id => {
    document.getElementById(id).addEventListener("change", enviarDatos);
});

// Botón dispensar
document.getElementById("btnDispensar").addEventListener("click", enviarDispensar);

// Actualiza datos cada 3 segundos
setInterval(obtenerDatos, 3000);

// Carga inicial
obtenerDatos();
