odoo.define('web.ListView.inherited', function (require) {
"use strict";

    var View = require('web.ListView');

    var ListView = View.extend({
        init: function (parent, dataset, view_id, options) {
                this._super(parent);
                this.set_default_options(options);
        },

        set_default_options: function(options) {
            this._super(options);
            _.defaults(this.options, {
                //whether the editable property of the view has to be disabled
                'disable_editable_mode': false,
                'limit': 122,
                });
         },
    }) ;
//alert('qsc');
return ListView;});




