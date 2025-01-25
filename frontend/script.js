const map = L.map('map').setView([51.505, -0.09], 13);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

async function loadTraffic() {
    const response = await fetch('http://localhost:5000/api/traffic');
    const data = await response.json();
    
    data.forEach(point => {
        L.marker([point.lat, point.lng])
            .bindPopup(`${point.Junction}<br>Vehicles: ${point.Vehicles}`)
            .addTo(map);
    });
}

async function simulate(junction) {
    const response = await fetch('http://localhost:5000/api/simulate', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ junction })
    });
    const data = await response.json();
    console.log('Simulation Result:', data);
}

loadTraffic();