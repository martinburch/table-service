// Function to cache spreadsheet to s3 with table-service server
// Call on-demand or however you like
function cacheChanges() {
  var key = SpreadsheetApp.getActiveSpreadsheet().getId();
  
     var payload =
   {
     "key" : key
   };
  
     var options =
   {
     "method" : "post",
     "payload" : payload
   };
  
   UrlFetchApp.fetch("http://example.com/cgi-bin/table-service/server.py", options);
  
}

// This cache may save a "short" version of your spreadsheet's key
// You can check it with a menu option

function onOpen() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var menuEntries = [ {name: "Get key...", functionName: "getCode"} ];
  ss.addMenu("Key", menuEntries);
}

function getCode() {
  var key = SpreadsheetApp.getActiveSpreadsheet().getId();
  var msg = key;
  
  Browser.msgBox(msg);
}