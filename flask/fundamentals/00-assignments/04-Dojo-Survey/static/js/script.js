var button=document.getElementById('submit')
var buttonHover=document.getElementById('submitHover')

function hover(element){
    console.log("hover activated")
    document.getElementById(element).id='submitHover'
}

function hoverOut(element){
    console.log("hover out!")
}