/* convert ul into listview */
$("[data-role=panel] ul").listview();

/* external panel is used in the demo
   therefore, it should be enhanced manually
   in addition to all contents inside it */
$("[data-role=panel]").enhanceWithin().panel();
