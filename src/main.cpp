
#include <Arduino.h>
#include <WiFi.h>
#include "wifi_config.h"
#include "defs.h"
#include <esp_wifi.h>
#include <HTTPClient.h>

void create_wifi_hotspot(){
  
  debugln("[+] Creating access point...");

  WiFi.softAP(SSID, PASSWORD);

  debugln("[+] Access point created with IP gateway"); 
  debug(WiFi.softAPIP());
}

void display_connected_devices(){
  /*
    This function lists all devices connected to this ESP access point
  */
  wifi_sta_list_t wifi_sta_list;
  tcpip_adapter_sta_list_t adapter_sta_list;
  esp_wifi_ap_get_sta_list(&wifi_sta_list);
  tcpip_adapter_get_sta_list(&wifi_sta_list, &adapter_sta_list);

  if(adapter_sta_list.num > 0){
    debugln("[+] Listing connected devices...");
  }

  for(uint8_t i = 0; i < adapter_sta_list.num; i++){
    tcpip_adapter_sta_info_t station = adapter_sta_list.sta[i];
    debugln( (String) "[+] Device ");
    debug(i);
  }
}


void setup() {
  Serial.begin(115200);
  create_wifi_hotspot();
  // display_connected_devices();
}

void loop() {
  // create a HTTP client object
  HTTPClient client;

  client.begin("http://192.168.4.2/get_roll");
  int http_code = client.GET(); // get the response code from the server


  if(http_code > 0){
    // success
    String payload = client.getString();
    debugln(http_code);
    debugln(payload);
  } else{
    debugln("[-] Error response code");
  }

  // free resources
  client.end();

}