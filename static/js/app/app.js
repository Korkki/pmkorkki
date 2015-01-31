"use strict";

var pmApp = angular.module('pmApp', [
    'restangular',
    'ui.bootstrap'
]);

var pmAppConfig = function (RestangularProvider) {
    RestangularProvider.setBaseUrl('/api');
    RestangularProvider.setRequestSuffix('/');
    RestangularProvider.setDefaultHeaders({Authorization: 'Token ' + window['token']});
    RestangularProvider.addResponseInterceptor(function(data, operation, what, url, response, deferred) {
        var extractedData;
        if (operation === "getList") {
            extractedData = data.results;
            extractedData.meta = _.omit(data, 'results');
        } else {
            extractedData = data.data;
        }
        return extractedData;
    });
};

pmAppConfig.$inject = ['RestangularProvider'];
pmApp.config(pmAppConfig);
