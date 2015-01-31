"use strict";

var pmApp = angular.module('pmApp', [
    'restangular'
]);

var pmAppConfig = function (RestangularProvider) {
    RestangularProvider.setBaseUrl('/api');
    RestangularProvider.setRequestSuffix('/');
    RestangularProvider.setDefaultHeaders({Authorization: 'Token c9d9884cedbb926678d3b7780e7bdd6735a9a242'});
};

pmAppConfig.$inject = ['RestangularProvider'];
pmApp.config(pmAppConfig);
