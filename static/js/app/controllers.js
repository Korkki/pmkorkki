"use strict";

var TopMenuController = function ($scope) {
    $scope.isCollapsed = true;
};

var TodoController = function ($scope, Restangular) {
    var items = Restangular.all('todo');
    items.getList().then(function (items) {
        $scope.todos =  items;
    });
};

TopMenuController.$inject = ['$scope'];
TodoController.$inject = ['$scope', 'Restangular'];

pmApp.controller('TopMenuController', TopMenuController);
pmApp.controller('TodoController', TodoController);
