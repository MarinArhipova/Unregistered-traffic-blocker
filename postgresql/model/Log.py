class Log():

    def __init__(self, log_time, user_name, database_name, process_id, connection_from, session_id,
                 session_line_num, command_tag, session_start_time, virtual_transaction_id, transaction_id,
                 error_severity, sql_state_code, message, detail, hint, internal_query, internal_query_pos,
                 context, query, query_pos, location, application_name):
        self.log_time = log_time
        self.user_name = user_name
        self.database_name = database_name
        self.process_id = process_id
        self.connection_from = connection_from
        self.session_id = session_id
        self.session_line_num = session_line_num
        self.command_tag = command_tag
        self.session_start_time = session_start_time
        self.virtual_transaction_id = virtual_transaction_id

        self.transaction_id = transaction_id
        self.error_severity = error_severity
        self.sql_state_code = sql_state_code
        self.message = message

        self.detail = detail
        self.hint = hint
        self.internal_query = internal_query
        self.internal_query_pos = internal_query_pos
        self.context = context
        self.query = query
        self.query_pos = query_pos
        self.location = location
        self.application_name = application_name