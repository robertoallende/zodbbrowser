// bottom panel 
var emptyBottom = function(){
    $("#bottom").text("");
    };

var bottom = function(nodepath) {
    $.ajax({
          url: nodepath + "/" + elem + "/get_source"  ,
          success: function(data) {
            $('#bottom').html(data);
            console.log('Load was performed.');
           }
     });
};

// right panel 
var emptyRight = function(){
    $("#right").text("");
    };

var right = function(nodepath, kind){
    $("#right").dynatree({
          initAjax: {
              url: nodepath + kind,
              data: { mode: "funnyMode" },
              dataType: "json"
              },
      onActivate: function(node) {
        elem = node.data.title;
        bottom(nodepath, elem);
      },
      onDeactivate: function(node) {
        // console.log("-");
      }
    });
  };

// midle panel 
var emptyMiddle = function(){
    $("#middle").text("");
    };

var middle = function(path){
    $("#middle").dynatree({
          initAjax: {
              url: path + "/list_kind",
              data: { mode: "funnyMode" },
              dataType: "json"
              },
      onActivate: function(node) {
        switch (node.data.title) {
            case "Properties" : right(path, '/properties') ;  break;
            case "Callables" : right(path, '/callables') ; break;
            case "Properties and Callables" : right(path, 'properties_and_callables');
                  break;
            case "Interfaces Provided" : right(path, '/properties') ; break;
            case "Adapts" : right(path, '/properties') ; break;
            case "Class and Ancestors" : right(path, '/class_ancestors') ; break;
        }
        // XXX this forces a request twice sometimes
        var rightTree = $("#right").dynatree("getTree");
        rightTree.reload();
      },
      onDeactivate: function(node) {
        emptyRight();
        emptyBottom();
      }
    });
  };


// Just for the left: getPath builds the path traversing the tree
var getPath = function(node) {
    if (node.data.title) { return ( getPath(node.parent) + "/" + node.data.title) ; }
    else { return "" ; }
};

// left panel
  $(function(){
    $("#left").dynatree({
          initAjax: {
              url: "/tree",
              data: { mode: "funnyMode" },
              dataType: "json"
              },
      onActivate: function(node) {
        middle(getPath(node));
        // XXX this forces a request twice sometimes
        var rightTree = $("#middle").dynatree("getTree");
        rightTree.reload();
      },
      onDeactivate: function(node) {
        emptyRight();
        emptyMiddle();
        emptyBottom();
      },
      onLazyRead: function(node){
                node.appendAjax({
                url: function() { return getPath(node) + "/tree"; }(),
                data: {key: node.data.key,
                       mode: "funnyMode"
                       }
              });
      }
    });
  });


