odoo.define('digizilla.digizilla_hide_create_button', function (require) {
    "use strict";

    var FormController = require('web.FormController');
    var core = require('web.core');
    var Dialog = require('web.Dialog');
    var framework = require('web.framework');

    var _t = core._t;

    FormController.include({
        renderButtons: function ($node) {
            this._super.apply(this, arguments);
            if (this.$buttons) {
                // Hide the "Create" button
                this.$buttons.find('.o-list-button-add').hide();
                this.$buttons.find('.o_form_button_save').hide();
                this.$buttons.find('.o-kanban-button-new').hide();
            }
        },
    });
});
