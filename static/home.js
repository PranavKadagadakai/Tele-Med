function convert() {
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function() {
        data=JSON.parse(this.responseText).data
      document.getElementById("text").innerHTML = data;
    }
    xhttp.open("GET", "getdata/"+document.getElementById("input").value, true);
    xhttp.send();
  }