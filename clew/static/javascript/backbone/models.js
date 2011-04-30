/**
 * Created by Clew.
 * User: svankiE
 * Date: 30/04/11
 * Time: 03:12
 * To change this template use File | Settings | File Templates.
 */

var Event = Backbone.Model.extend({
    initialize: function(attrs, options) {
        this.title = attrs.title || "No title";
        this.description = attrs.description || "No description";
        this.date = attrs.date || "No date";
    }
    // other methods
});

var EventStore = Backbone.Collection.extend({
    model: Event
});

/** this must be in the behavior.js */
var events = new EventStore({
    // JSON from controller
});