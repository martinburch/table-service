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
