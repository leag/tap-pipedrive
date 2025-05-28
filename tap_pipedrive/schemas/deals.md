title
string
required
The title of the deal

owner_id
integer
The ID of the user who owns the deal

person_id
integer
The ID of the person linked to the deal

org_id
integer
The ID of the organization linked to the deal

pipeline_id
integer
The ID of the pipeline associated with the deal

stage_id
integer
The ID of the deal stage

value
number
The value of the deal

currency
string
The currency associated with the deal

add_time
string
The creation date and time of the deal

update_time
string
The last updated date and time of the deal

stage_change_time
string
The last updated date and time of the deal stage

is_deleted
boolean
Whether the deal is deleted or not

is_archived
boolean
Whether the deal is archived or not

archive_time
string
The optional date and time of archiving the deal in UTC. Format: YYYY-MM-DD HH:MM:SS. If omitted and is_archived is true, it will be set to the current date and time.

status
string
The status of the deal

probability
number
The success probability percentage of the deal

lost_reason
string
The reason for losing the deal. Can only be set if deal status is lost.

visible_to
integer
The visibility of the deal

close_time
string
The date and time of closing the deal. Can only be set if deal status is won or lost.

won_time
string
The date and time of changing the deal status as won. Can only be set if deal status is won.

lost_time
string
The date and time of changing the deal status as lost. Can only be set if deal status is lost.

expected_close_date
string
The expected close date of the deal

Formatdate
label_ids
array
The IDs of labels assigned to the deal