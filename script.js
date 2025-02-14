document.addEventListener("DOMContentLoaded", () => {
    const authScreen = document.getElementById("authScreen");
    const mainContent = document.getElementById("mainContent");
    const loginForm = document.getElementById("loginForm");
    const registerForm = document.getElementById("registerForm");
    const showRegister = document.getElementById("showRegister");
    const showLogin = document.getElementById("showLogin");
    const loginUsername = document.getElementById("loginUsername");
    const loginPassword = document.getElementById("loginPassword");
    const registerUsername = document.getElementById("registerUsername");
    const registerPassword = document.getElementById("registerPassword");
    const themeToggle = document.getElementById("themeToggle");
    const countrySelect = document.getElementById("country");
    const citySelect = document.getElementById("city");
    const getWeatherBtn = document.getElementById("getWeather");
    const weatherInfo = document.getElementById("weatherInfo");
    const outfitSuggestion = document.getElementById("outfitSuggestion");
    const sundaySubjectsInput = document.getElementById("sundaySubjects");
    const mondaySubjectsInput = document.getElementById("mondaySubjects");
    const tuesdaySubjectsInput = document.getElementById("tuesdaySubjects");
    const wednesdaySubjectsInput = document.getElementById("wednesdaySubjects");
    const thursdaySubjectsInput = document.getElementById("thursdaySubjects");
    const fridaySubjectsInput = document.getElementById("fridaySubjects");
    const saturdaySubjectsInput = document.getElementById("saturdaySubjects");
    const saveScheduleBtn = document.getElementById("saveSchedule");
    const tomorrowReminder = document.getElementById("tomorrowReminder");
    const setReminderBtn = document.getElementById("setReminder");
    const reminderDisplay = document.getElementById("reminderDisplay");

    const users = [];
    let currentUser = null;

    showRegister.addEventListener("click", () => {
        loginForm.classList.add("hidden");
        registerForm.classList.remove("hidden");
    });

    showLogin.addEventListener("click", () => {
        registerForm.classList.add("hidden");
        loginForm.classList.remove("hidden");
    });

    loginForm.addEventListener("submit", (event) => {
        event.preventDefault();
        const username = loginUsername.value;
        const password = loginPassword.value;

        currentUser = users.find(user => user.username === username && user.password === password);

        if (currentUser) {
            authScreen.style.display = "none";
            mainContent.style.display = "block";
        } else {
            alert("פרטי התחברות שגויים");
        }
    });

    registerForm.addEventListener("submit", (event) => {
        event.preventDefault();
        const username = registerUsername.value;
        const password = registerPassword.value;

        if (users.some(user => user.username === username)) {
            alert("השם כבר קיים");
        } else {
            users.push({ username, password });
            alert("הרישום הצליח!");
            showLogin.click();
        }
    });

    getWeatherBtn.addEventListener("click", async () => {
        const city = citySelect.value;
        const country = countrySelect.value;

        if (city && country) {
            try {
                const response = await fetch(`https://api.weatherapi.com/v1/current.json?key=bfba7f78869e4222b89154845251302&q=${city},${country}`);
                const weather = await response.json();
                weatherInfo.textContent = `מזג האוויר ב-${city}: ${weather.current.temp_c}°C, ${weather.current.condition.text}`;
                suggestOutfit(weather);
            } catch (error) {
                alert("שגיאה בטעינת מזג האוויר");
            }
        } else {
            alert("בחר עיר ומדינה");
        }
    });

    function suggestOutfit(weather) {
        let suggestion = "";
        if (weather.current.temp_c < 10) {
            suggestion = "קר מאוד! כדאי לקחת מעיל וצעיף.";
        } else if (weather.current.temp_c < 20) {
            suggestion = "קצת קריר! מעיל קל יהיה טוב.";
        } else {
            suggestion = "חמים! תלבש משהו קל.";
        }

        if (weather.current.condition.text.toLowerCase().includes("rain")) {
            suggestion += " אל תשכח מטרייה!";
        }

        outfitSuggestion.textContent = suggestion;
    }

    saveScheduleBtn.addEventListener("click", () => {
        const schedule = {
            sunday: sundaySubjectsInput.value.trim(),
            monday: mondaySubjectsInput.value.trim(),
            tuesday: tuesdaySubjectsInput.value.trim(),
            wednesday: wednesdaySubjectsInput.value.trim(),
            thursday: thursdaySubjectsInput.value.trim(),
            friday: fridaySubjectsInput.value.trim(),
            saturday: saturdaySubjectsInput.value.trim(),
        };

        localStorage.setItem("weeklySchedule", JSON.stringify(schedule));
        alert("לוח הזמנים נשמר!");
    });

    setReminderBtn.addEventListener("click", () => {
        const reminder = tomorrowReminder.value.trim();
        localStorage.setItem("tomorrowReminder", reminder);
        reminderDisplay.textContent = `תזכורת: ${reminder}`;
    });

    const savedSchedule = JSON.parse(localStorage.getItem("weeklySchedule"));
    if (savedSchedule) {
        sundaySubjectsInput.value = savedSchedule.sunday;
        mondaySubjectsInput.value = savedSchedule.monday;
        tuesdaySubjectsInput.value = savedSchedule.tuesday;
        wednesdaySubjectsInput.value = savedSchedule.wednesday;
        thursdaySubjectsInput.value = savedSchedule.thursday;
        fridaySubjectsInput.value = savedSchedule.friday;
        saturdaySubjectsInput.value = savedSchedule.saturday;
    }

    const savedReminder = localStorage.getItem("tomorrowReminder");
    if (savedReminder) {
        reminderDisplay.textContent = `תזכורת: ${savedReminder}`;
    }

    themeToggle.addEventListener("click", () => {
        document.body.classList.toggle("dark-mode");
    });
});
