$(function () {
	$("#tree").jstree({ 
		"json_data" : {
			"ajax" : { "url" : "tree",
                       "dataType" : "json",
                       "async" : true, 
                       "data" : (function() { console.log('hola'); })
                   },
            "progressive_render" : true,
            "error": this.onError,
            "success": this.onSuccess
		},
		"plugins" : [ "themes", "json_data" ]
	});
});

