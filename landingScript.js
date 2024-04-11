function increaseFontSize(increaseFactor) {
    
    //Increase all Header 1 text by desired amount 
    txtH1 = document.getElementById('text');
    style = window.getComputedStyle(txtH1, null).getPropertyValue('font-size');
    currentSize = parseFloat(style);
    txtH1.style.fontSize = (currentSize + increaseFactor) + 'px';
}

function increaseBodyFontSize(fontsize){
    
    if(fontsize == 20){
        document.getElementById("p2").style.color = "blue";
    }
}

function changeStyle(option){
    console.log("test", option)
    if (option == 'A'){
        //add class and change the class based off button 
        document.querySelector('link').setAttribute('href', 'landingStyle.css');
    }
    else{
        document.querySelector('link').setAttribute('href', 'style.css');
    }
}


function changeFontColour(option) {

    //Increase all Header 1 text by desired amount 
    txt = document.getElementById("text")
    style = window.getComputedStyle(txtH1, null).getPropertyValue('font-size');
    if (option == 1){
        txtH1.style.changeFontColour = '#000000'
    }
    else{
        txtH1.style.changeFontColour = '#100763'
    }

}

function removeDiv(id){
    document.getElementById(id).style.visibility = "hidden";
}