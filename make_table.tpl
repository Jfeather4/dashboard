%#template
<p>Status Home Page</p>
<div id="home">
<table border="1">
  <tr>
    <th>Item</th>
    <th>Status</th>
    <th>Detail</th>
  </tr>
%for key, value in results.items():
  <tr>
    <td>{{key}}</td>
    <td>{{value['status']}}</td>
    <td><a href="{{value['link']}}">Link to endpoint</a></td>
  </tr>
%end
</table>
<button type="button" onclick="loadDoc()">Refresh</button>
</div>

<script>
function loadDoc() {
  const xhttp = new XMLHttpRequest();
  xhttp.onload = function() {
    document.getElementById("home").innerHTML =
    this.responseText;
  }
  xhttp.open("GET", "ajax_info.txt");
  xhttp.send();
}
</script>