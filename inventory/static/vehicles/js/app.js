async function loadVehicles() {

    try {

        const response = await fetch(
            "/api/vehicles/"
        );

        const vehicles =
            await response.json();


        const container =
            document.getElementById(
                "vehicle-container"
            );


        container.innerHTML = "";


        if (vehicles.length === 0) {

            container.innerHTML = `

                <p class="no-vehicles">
                    No vehicles available.
                </p>

            `;

            return;
        }


        vehicles.forEach(function(vehicle) {

            const card =
                document.createElement("div");

            card.className = "vehicle-card";


            card.innerHTML = `

                <div class="car-image">
                    🚗
                </div>


                <div class="vehicle-info">

                    <h3>
                        ${vehicle.brand}
                        ${vehicle.name}
                    </h3>


                    <p>
                        Year: ${vehicle.year}
                    </p>


                    <p>
                        Fuel: ${vehicle.fuel_type}
                    </p>


                    <h4>
                        ₹${vehicle.price_per_day}
                        / day
                    </h4>


                    <div class="status">

                        ${
                            vehicle.is_available
                            ?
                            `
                            <span class="available">
                                Available
                            </span>
                            `
                            :
                            `
                            <span class="unavailable">
                                Unavailable
                            </span>
                            `
                        }

                    </div>


                    <a
                        href="/vehicle/${vehicle.id}/"
                        class="details-button"
                    >
                        View Details
                    </a>

                </div>

            `;


            container.appendChild(card);

        });

    }

    catch (error) {

        document.getElementById(
            "vehicle-container"
        ).innerHTML = `

            <p class="error">
                Could not load vehicles.
            </p>

        `;

    }

}


loadVehicles();