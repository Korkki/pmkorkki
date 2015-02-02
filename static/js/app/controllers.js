"use strict";

var TopMenuController = function ($scope) {
    $scope.isCollapsed = true;
};

var FormController = function ($scope, $modalInstance, form) {
    $scope.form = form;

    $scope.close = function () {
        $modalInstance.dismiss('close');
    };

    $scope.sendForm = function (form) {
        if (form.$valid) {
            $modalInstance.close($scope.form);
        }
    };
};

var TodoController = function ($scope, Restangular, $modal) {
    var items = Restangular.all('todo');
    items.getList().then(function (items) {
        $scope.todos =  items;
    });

    $scope.todoModal = function (id, size) {
        var form = {};
        var modalInstance = $modal.open({
            templateUrl: window['templates'] + '/todo/add_todo.modal.html',
            controller: FormController,
            size: size,
            resolve: {
                form: function () {
                    return form;
                }
            }
        });

        modalInstance.result.then(function (form) {
            form.author = window['user'];
            items.post(form);
        });
    };

    $scope.done = function (i, id) {
        $scope.todos[i].done = true;
        Restangular.one('todo', id).patch({done: true});
    };

    $scope.delItem = function (i, id) {
        Restangular.one('todo', id).remove();
        $scope.todos.splice(i, 1);
    };
};

TopMenuController.$inject = ['$scope'];
TodoController.$inject = ['$scope', 'Restangular', '$modal'];
FormController.$inject = ['$scope', '$modalInstance', 'form'];

pmApp.controller('TopMenuController', TopMenuController);
pmApp.controller('TodoController', TodoController);
