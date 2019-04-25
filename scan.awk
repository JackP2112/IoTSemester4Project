$1 == "BSS" {
	i = $2	
}
$1 == "capability:" {
	if($0 !~ ".*Privacy.*"){
		results[i]["sec"] = "Open"
	}
}
$1 == "signal:" {
	results[i]["sig"] = $2
}
$1 == "SSID:" {
	results[i]["ssid"] = $2
}
$1 == "RSN:" {
	if(results[i]["sec"] == 0){
		results[i]["sec"] = "WPA2"
	}
}
$1 == "WPA:" {
	if(results[i]["sec"] == 0){
		results[i]["sec"] = "WPA"
	}
}
END {
	for(r in results){
		if(results[r]["sec"] == 0) { results[r]["sec"] = "WEP"}
		printf "%s %s %s\n",results[r]["ssid"],results[r]["sec"],results[r]["sig"]	
	}
}
