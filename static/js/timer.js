/**
 * Created by GPRA360 on 09.01.2017.
 */

var bell = new Audio('/static/sounds/bowl_sound.wav'),
    timeInterval;

function getTimeRemaining(endtime){
    var t = Date.parse(endtime) - Date.parse(new Date());
    var seconds = Math.floor((t / 1000) % 60);
    var minutes = Math.floor((t / 1000 / 60) % 60);
    var hours = Math.floor(t / (1000 * 60 * 60) % 24);
    return {
        'total': t,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds
    };
}

function showSaveFunctions(totalTime) {
        $('#save').show();
        $('#saveTimeP').show();
        $('#saveTimeP').text("You meditated " + (totalTime.total / 1000 / 60) + " minute(s).");
}

function initializeClock(id, endtime){
    var clock = document.getElementById(id),
        hoursSpan = clock.querySelector('.hours'),
        minutesSpan = clock.querySelector('.minutes'),
        secondsSpan = clock.querySelector('.seconds'),
        totalTime = getTimeRemaining(endtime);

    function updateClock(){
        var t = getTimeRemaining(endtime);

        hoursSpan.innerHTML = ('0' + t.hours).slice(-2);
        minutesSpan.innerHTML = ('0' + t.minutes).slice(-2);
        secondsSpan.innerHTML = ('0' + t.seconds).slice(-2);

        if(t.total <= 0){
            bell.play();
            clearInterval(timeInterval);
            showSaveFunctions(totalTime);
        }
    }

    updateClock();
    timeInterval = setInterval(updateClock, 1000);
}

function onStartTimerBtnPress(){
    var selectedTime = document.getElementById("timeInput").value,
        currentTime = Date.parse(new Date()),
        deadline = new Date(currentTime + selectedTime*60*1000);

    if(selectedTime <= 0 || selectedTime == null){
        alert('Please enter a valid time!');
    }else{
        clearInterval(timeInterval);
        initializeClock('clockdiv', deadline);
    }
}