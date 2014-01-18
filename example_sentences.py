import urllib2
#from BeautifulSoup import BeautifulSoup
# or if you're using BeautifulSoup4:
from bs4 import BeautifulSoup



html_doc = """

<html>
<head>
<title>Beispiels&auml;tze-Datenbank Englisch Deutsch</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">

<style><!--
body,td,a,p,.h{font-family:arial,sans-serif;}
.h{font-size: 20px;}
.q{color:#0000cc;}
//-->
</style>

<script language="JavaScript" type="text/javascript">
<!-- Hide
function setFocus()
{
  document.form1.q.focus();
  document.form1.q.select();
}

// -->
</script>

</head>

<body bgcolor="#FFFFFF" text="#000000" onLoad=setFocus()>
<table width="90%" border="0" align="center">
  <tr> 
    <td> 
      <div align="center"><h1><a href="/bs/">Beispiels&auml;tze-Datenbank Englisch Deutsch</a></h1>
      
      <!-- AddThis Bookmark Button BEGIN -->
<script type="text/javascript">
  addthis_url    = location.href;   
  addthis_title  = document.title;  
  addthis_pub    = 'natmedtalk';     
</script><script type="text/javascript" src="http://s7.addthis.com/js/addthis_widget.php?v=12" ></script>
<!-- AddThis Bookmark Button END -->
      
      </div>
    </td>
  </tr>
  <tr> 

    <td align="center">
    <br>
<script type="text/javascript"><!--
google_ad_client = "pub-5282921004649140";
google_ad_width = 728;
google_ad_height = 90;
google_ad_format = "728x90_as";
google_ad_type = "text_image";
google_ad_channel ="";
//--></script>
<script type="text/javascript"
  src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
</script>
    <br><br>
    </td> 

  </tr>
    <tr> 
    <td> 
      <form name="form1" method="get" action="index.php">
        <p align="center"> <font size="-1"> 
          <input type="text" name="q" 
          value="as " 
          maxlength="50" size="50">
          <input type="submit" name="submit" value="Suchen">
          <br>
                    <input type="radio" name="lang" value="en" checked>
          Englisch 
          <input type="radio" name="lang" value="de" >
          Deutsch<br>
          </font></p>
      </form>
    </td>
  </tr>
  <tr> 
    <td> <font size="-1"> 
      <table width=100% border=1 align=center  bordercolor=#a6bddc>
<tr><td><div align=center><b><font size=-1>Englisch<font></b></div></td><td><div align=center><b><font size=-1>Deutsch<font></b></div></td></tr>
<tr><td><font size=-1>Her list of wishes is <b>as </b>long as your arm.</font></td><td><font size=-1>Ihr Wunschzettel ist ellenlang.<font></td></tr>
<tr><td><font size=-1>The work is not <b>as </b>difficult as you imagine.</font></td><td><font size=-1>Die Arbeit ist nicht so schwer, wie du dir vorstellst.<font></td></tr>
<tr><td><font size=-1><b>As </b>she left the room she remembered the book.</font></td><td><font size=-1>Als sie aus dem Zimmer ging, fiel ihr das Buch wieder ein.<font></td></tr>
<tr><td><font size=-1>I'm just <b>as </b>clever as you.</font></td><td><font size=-1>Ich bin genauso klug wie du.<font></td></tr>
<tr><td><font size=-1>His greatness <b>as </b>a writer is unquestioned.</font></td><td><font size=-1>Seine Bedeutung als Schriftsteller ist unbestritten.<font></td></tr>
<tr><td><font size=-1>I can offer my land <b>as </b>a guarantee.</font></td><td><font size=-1>Ich kann mein Land als Garantie anbieten.<font></td></tr>
</table>      </font></td>
  </tr>
  <tr> 
    <td><font size="-1"></font> </td>
  </tr>
  <tr> 
    <td> 
      <div align="left"><font size="-1">*Bitte beachten: die Suchfunktion pr&uuml;ft 
        exakte &Uuml;bereinstimmung, es wird auch nach Leerzeichen gesucht: &#132;test&#147;, 
        &#132; test&#147; und &#132; test &#132; bringen unterschiedliche Ergebnisse.</font></div>
    </td>
  </tr>
  <tr>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td>
      <div align="center"><font size="-1">Wir freuen uns &uuml;ber <a href="../contact.php">Vorschl&auml;ge, 
        Kommentare und Kritik</a>. Jedes Feedback ist uns willkommen.</font></div>
    </td>
  </tr>
  <tr> 
    <td> 
      <div align="center"><font size="-2"><a href="/">Vokaboly.de</a> 
        &copy; 2003-2007</font></div>
    </td>
  </tr>
</table>
</body>
</html>
"""

soup = BeautifulSoup(html_doc)
#soup = BeautifulSoup(urllib2.urlopen('http://www.vokaboly.de/bs/index.php?q=as+&submit=Suchen&lang=en').read())
content = soup('table')[1]
rows = content.find_all('tr')[1:]
for row in rows:
  english, german = row.find_all('font')[:2]
  print ''.join(english.findAll(text=True))
  print ''.join(german.findAll(text=True))
