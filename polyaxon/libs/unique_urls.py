def get_user_url(username):
    return '/{}'.format(username)


def get_project_url(unique_name):
    values = unique_name.split('.')
    return '{}/{}'.format(get_user_url(values[0]), values[1])


def get_user_project_url(username, project_name):
    return '{}/{}'.format(get_user_url(username), project_name)


def get_experiment_url(unique_name):
    values = unique_name.split('.')
    project_url = get_user_project_url(username=values[0], project_name=values[1])
    return '{}/experiments/{}'.format(project_url, values[-1])


def get_experiment_health_url(unique_name):
    experiment_url = get_experiment_url(unique_name=unique_name)
    return '{}/_heartbeat'.format(experiment_url)


def get_experiment_group_url(unique_name):
    values = unique_name.split('.')
    project_url = get_user_project_url(username=values[0], project_name=values[1])
    return '{}/groups/{}'.format(project_url, values[-1])


def get_job_url(unique_name):
    values = unique_name.split('.')
    project_url = get_user_project_url(username=values[0], project_name=values[1])
    return '{}/jobs/{}'.format(project_url, values[-1])


def get_job_health_url(unique_name):
    job_url = get_job_url(unique_name=unique_name)
    return '{}/_heartbeat'.format(job_url)


def get_build_url(unique_name):
    values = unique_name.split('.')
    project_url = get_user_project_url(username=values[0], project_name=values[1])
    return '{}/builds/{}'.format(project_url, values[-1])
