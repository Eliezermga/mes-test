/*const pi = 3.14;
    pi = 1;
    console.log(pi)

var a = 3;
    a = 3;
    console.log(a)
console.log(30*24*60*60)

var L = 14;
var l = 8;
aire = L*l;
console.log(aire)

var b = "unh";
    console.log(`ici c'est ${b}`);


 entrez = prompt("entrer le solde de votre solde");
 retrait = prompt("montant à retirer");
 solde = entrez - retrait;
 alert ("vous avez retirez "+retrait  +" votre solde est de :" +solde);


v = prompt("Entrez  la couleur");
    if(v == "rouge"){
        alert("casse#1");
    }
    else{
        if (v== "vert") {
            alert("case#2")
        }
        else{
            if(v== "noir"){
            alert("case#3")
            }
            else{
                alert("inconnu")
            }
        }
       
}
    a = prompt("valeur voulue")
    n = a+1
    while (a<n) {
     alert("ça marche")   
    }   


    s = prompt("saisire les secondes");
    n = 0
while (s > n){
    s=s-1
    alert(s)
}

var sec = 90;
while(sec >= 0){
    console.log(sec);
    sec--;
}


var m = prompt("entrez la valeur")
while(m < 10000){
    m= m*10
    alert("le resulat est : " +m)
    break
}*/

var m= prompt("entrez la valeur");

for (var i =0; i < 10000; i*10) {
 if (m == 10000)
   break 
   alert(m)
 m += i
}