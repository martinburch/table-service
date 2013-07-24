// Function to cache spreadsheet to s3 with table-service server
// Automatically called on edit, but change the function name
// to call it whenever you want

function onEdit() {
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
