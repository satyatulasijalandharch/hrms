"""
urls.py

This page is used to map request or url path with function

"""
from django.urls import path
import attendance.views.clock_in_out

import attendance.views.dashboard
import attendance.views.search
import attendance.views.requests
from .views import views

urlpatterns = [
    path("attendance-create", views.attendance_create, name="attendance-create"),
    path("attendance-excel", views.attendance_excel, name="attendance-excel"),
    path("attendance-info-import", views.attendance_import, name="attendance-info-import"),
    path("attendance-info-export", views.attendance_export, name="attendance-info-export"),
    path("attendance-view", views.attendance_view, name="attendance-view"),
    path(
        "attendance-search",
        attendance.views.search.attendance_search,
        name="attendance-search",
    ),
    path(
        "attendance-update/<int:obj_id>/",
        views.attendance_update,
        name="attendance-update",
    ),
    path(
        "attendance-delete/<int:obj_id>/",
        views.attendance_delete,
        name="attendance-delete",
    ),
    path(
        "attendance-bulk-delete",
        views.attendance_bulk_delete,
        name="attendance-bulk-delete",
    ),
    path(
        "attendance-overtime-create",
        views.attendance_overtime_create,
        name="attendance-overtime-create",
    ),
    path(
        "attendance-overtime-view",
        views.attendance_overtime_view,
        name="attendance-overtime-view",
    ),
    path(
        "attendance-overtime-search",
        attendance.views.search.attendance_overtime_search,
        name="attendance-ot-search",
    ),
    path(
        "attendance-overtime-update/<int:obj_id>/",
        views.attendance_overtime_update,
        name="attendance-overtime-update",
    ),
    path(
        "attendance-overtime-delete/<int:obj_id>/",
        views.attendance_overtime_delete,
        name="attendance-overtime-delete",
    ),
    path(
        "attendance-activity-view",
        views.attendance_activity_view,
        name="attendance-activity-view",
    ),
    path(
        "attendance-activity-search",
        attendance.views.search.attendance_activity_search,
        name="attendance-activity-search",
    ),
    path(
        "attendance-activity-delete/<int:obj_id>/",
        views.attendance_activity_delete,
        name="attendance-activity-delete",
    ),
    path("view-my-attendance", views.view_my_attendance, name="view-my-attendance"),
    path(
        "filter-own-attendance",
        attendance.views.search.filter_own_attendance,
        name="filter-own-attendance",
    ),
    path(
        "own-attendance-filter",
        attendance.views.search.own_attendance_sort,
        name="own-attendance-filter",
    ),
    path("clock-in", attendance.views.clock_in_out.clock_in, name="clock-in"),
    path("clock-out", attendance.views.clock_in_out.clock_out, name="clock-out"),
    path(
        "late-come-early-out-view",
        views.late_come_early_out_view,
        name="late-come-early-out-view",
    ),
    path(
        "late-come-early-out-search",
        attendance.views.search.late_come_early_out_search,
        name="late-come-early-out-search",
    ),
    path(
        "late-come-early-out-delete/<int:obj_id>/",
        views.late_come_early_out_delete,
        name="late-come-early-out-delete",
    ),
    path(
        "validation-condition-create",
        views.validation_condition_create,
        name="validation-condition-create",
    ),
    path(
        "validation-condition-update/<int:obj_id>/",
        views.validation_condition_update,
        name="validation-condition-update",
    ),
    path(
        "validation-condition-delete/<int:obj_id>/",
        views.validation_condition_delete,
        name="validation-condition-delete",
    ),
    path(
        "validate-bulk-attendance",
        views.validate_bulk_attendance,
        name="validate-bulk-attendance",
    ),
    path(
        "validate-this-attendance/<int:obj_id>/",
        views.validate_this_attendance,
        name="validate-this-attendance",
    ),
    path(
        "revalidate-this-attendance/<int:obj_id>/",
        views.revalidate_this_attendance,
        name="revalidate-this-attendance",
    ),
    path(
        "approve-overtime/<int:obj_id>/",
        views.approve_overtime,
        name="approve-overtime",
    ),
    path(
        "approve-bulk-overtime",
        views.approve_bulk_overtime,
        name="approve-bulk-overtime",
    ),
    path("dashboard", attendance.views.dashboard.dashboard, name="dashboard"),
    path(
        "dashboard-attendance",
        attendance.views.dashboard.dashboard_attendance,
        name="dashboard-attendance",
    ),
    path(
        "request-attendance",
        attendance.views.requests.request_attendance,
        name="request-attendance",
    ),
    path(
        "request-attendance-view",
        attendance.views.requests.request_attendance_view,
        name="request-attendance-view",
    ),
    path(
        "request-attendance/<int:attendance_id>/",
        attendance.views.requests.attendance_request_changes,
        name="attendance-change",
    ),
    path(
        "validate-attendance-request/<int:attendance_id>/",
        attendance.views.requests.validate_attendance_request,
        name="validate-attendance-request",
    ),
    path(
        "approve-validate-attendance-request/<int:attendance_id>/",
        attendance.views.requests.approve_validate_attendance_request,
        name="approve-validate-attendance-request",
    ),
    path(
        "edit-validate-attendance/<int:attendance_id>/",
        attendance.views.requests.edit_validate_attendance,
        name="edit-validate-attendance",
    ),
    path(
        "search-attendance-requests",
        attendance.views.search.search_attendance_requests,
        name="search-attendance-requests",
    ),
    path(
        "cancel-validate-attendance-request/<int:attendance_id>/",
        attendance.views.requests.cancel_attendance_request,
        name="cancel-validate-attendance-request",
    ),
    path(
        "request-new-attendance",
        attendance.views.requests.request_new,
        name="request-new-attendance",
    ),
    path("employee-widget-filter",attendance.views.search.widget_filter,name="attendance-widget-filter")
]
