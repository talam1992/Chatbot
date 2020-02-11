__author__ = 'Timothy Lam'

import requests
from bs4 import BeautifulSoup
import config
from multiprocessing.pool import ThreadPool
from threading import Thread
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import time
import os
pool = ThreadPool(processes=5)
cities = ["London", "Manchester", "Edinburgh", "Bristol", "Bath", "Birmingham", "Liverpool", "Glasgow"]
thread_result = [list(range(len(cities))), list(range(len(cities)))]    # [[min], [max]]


def selector(message):
    if message[:len("job search average salary for ")] == "job search average salary for ":
        query = message[len("job search average salary for "):].split(' in ')
        job = query[0].strip()
        place = query[1].strip()
        return average_salary(job,place)
    elif message[:len("job search min salary for ")] == "job search min salary for ":
        query = message[len("job search min salary for "):].split(' in ')
        job = query[0].strip()
        place = query[1].strip()
        return min_salary(job, place)
    elif message[:len("job search max salary for ")] == "job search max salary for ":
        query = message[len("job search max salary for "):].split(' in ')
        job = query[0].strip()
        place = query[1].strip()
        return max_salary(job, place)
    elif message[:len("job search average salary graph for ")] == "job search average salary graph for ":
        query = message[len("job search average salary graph for "):].split(' in ')
        job = query[0].strip()
        return average_salary_graph(job)
    else:
        return "Parrotlet is not in the mood to answer this job search related question"


def go_to(url):
    page = requests.get(url, headers=config.header)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup


def search_page(job, where):
    url = f"https://www.indeed.co.uk/jobs?q={job}&l={where}"
    page = requests.get(url, headers=config.header)
    soup = BeautifulSoup(page.content, 'html.parser')
    # items = soup.find_all("div", {"class": "jobsearch-jobDescriptionText"})
    items = soup.find_all("div", {"class": "jobsearch-SerpJobCard unifiedRow row result"})

    return items


def search_job(job, where):
    items = search_page(job, where)
    min_ = []
    max_ = []

    for job_post in items:
        try:
            salary_raw = job_post.find("span", {"class": "salaryText"}).get_text()

            if '-' in salary_raw:
                salary_raw = salary_raw.split('-')
                con = salary_raw[1].split()[-1].strip()
                if con == 'year':
                    multi = 1
                elif con == 'month':
                    multi = 12
                else:
                    multi = 5*4*12
                min_.append(float(salary_raw[0].strip()[1:].replace(',', ''))*multi)
                max_.append(float(salary_raw[1].split()[0].strip()[1:].replace(',', ''))*multi)
        except AttributeError:
            pass
    
    return min_, max_


def add_format(query):
    query = str(round(query, 2))
    raw = query.split('.')
    points = raw[1] if len(raw[1]) == 2 else raw[1]+'0'
    int_ = format(int(raw[0]), ',d')

    return f'{int_}.{points}'


def average_salary_raw(job, place, th=-1):
    min_, max_ = search_job(job, place)
    if len(min_) == 0:
        if th != -1:    # getting thread result
            thread_result[0][th] = 0
            thread_result[1][th] = 0
            #print('no')
        else:
            return 0
    else:
        avg_min = sum(min_) / len(min_)
        avg_max = sum(max_) / len(max_)
        if th != -1:    # getting thread result
            thread_result[0][th] = avg_min
            thread_result[1][th] = avg_max
            #print(thread_result)
        else:
            return avg_min, avg_max


def average_salary(job, place):
    result = average_salary_raw(job, place)
    if result == 0:
        return f"Rihanna could not find {job}"
    else:
        avg_min = add_format(result[0])
        avg_max = add_format(result[1])
        display = f"The average annual salary for {job} in {place.capitalize()} ranges from £{avg_min} to £{avg_max}"
        reply = {'display': display, 'say': display}
        return reply


def min_salary(job, place):
    # add min salary and job link
    items = search_page(job, place)
    min_ = {}    # {link: salary}
    min_comp = {}    # {link: company}
    for job_post in items:
        try:
            salary_raw = job_post.find("span", {"class": "salaryText"}).get_text()
            try:

                company = job_post.find("a", {"data-tn-element": "companyName"}).get_text()
            except AttributeError:
                company = job_post.find("span", {"class": "company"}).get_text()
                #company = job_post.find("a", {"class": "turnstileLink"}).get_text()
            link = job_post.find("a", {"class": "jobtitle turnstileLink"}).get('href')
            if '-' in salary_raw:
                salary_raw = salary_raw.split('-')
                con = salary_raw[1].split()[-1].strip()
                if con == 'year':
                    multi = 1
                elif con == 'month':
                    multi = 12
                else:
                    multi = 5 * 4 * 12
                min_[link] = float(salary_raw[0].strip()[1:].replace(',', '')) * multi
                min_comp[link] = company

        except AttributeError:
            pass
    if len(min_) > 0:
        min_job = min(min_, key=min_.get)
        h = '\n'
        reply = {'display': f'The Minimum Salary for {job} in {place} from indeed website is £{add_format(min_[min_job])} Annually. '
                            f'<br>This Job is offered by {min_comp[min_job].replace(h, "")}. '
                            f'<a href="https://www.indeed.co.uk{min_job}" target="_blank">view</a>',
                 'say': f'The Minimum Salary for {job} in {place} from indeed website is £{add_format(min_[min_job])} Annually. '
                            f'This Job is offered by {min_comp[min_job].replace(h, "")}. '
                            f'link is provided'}
        return reply
    else:
        return f"Rihanna could not find {job}"


def max_salary(job, place):
    items = search_page(job, place)
    max_ = {}    # {link: salary}
    max_comp = {}    # {link: company}
    for job_post in items:
        try:
            salary_raw = job_post.find("span", {"class": "salaryText"}).get_text()
            try:

                company = job_post.find("a", {"data-tn-element": "companyName"}).get_text()
            except AttributeError:
                company = job_post.find("span", {"class": "company"}).get_text()
                #company = job_post.find("a", {"class": "turnstileLink"}).get_text()
            link = job_post.find("a", {"class": "jobtitle turnstileLink"}).get('href')
            if '-' in salary_raw:
                salary_raw = salary_raw.split('-')
                con = salary_raw[1].split()[-1].strip()
                if con == 'year':
                    multi = 1
                elif con == 'month':
                    multi = 12
                else:
                    multi = 5 * 4 * 12
                max_[link] = float(salary_raw[1].split()[0].strip()[1:].replace(',', ''))*multi
                max_comp[link] = company

        except AttributeError:
            pass
    if len(max_) > 0:
        min_job = max(max_, key=max_.get)
        h = '\n'
        reply = {'display': f'The Maximum Salary for {job} in {place} from indeed website is £{add_format(max_[min_job])} Annually. '
                            f'<br>This Job is offered by {max_comp[min_job].replace(h, "")}. '
                            f'<a href="https://www.indeed.co.uk{min_job}" target="_blank">view</a>',
                 'say': f'The Maximum Salary for {job} in {place} from indeed website is £{add_format(max_[min_job])} Annually. '
                            f'This Job is offered by {max_comp[min_job].replace(h, "")}. '
                            f'link is provided'}
        return reply
    else:
        return f"Rihanna could not find {job}"


def k_format(x):
    return round(x/1000, 1)


def salary_plot(cities_min, cities_max, job):
    #print(f'values:{cities_min}\n{cities_max}')
    width = 0.35
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ind = np.arange(len(cities_max))
    p1 = ax.bar(ind, cities_min, width, color='r', alpha=0.3)
    p2 = ax.bar(ind, np.array(cities_max) - np.array(cities_min), width, color='g', bottom=cities_min, alpha=0.3)
    ax.set_xticks(ind)
    ax.set_xticklabels(cities)
    for i in range(len(cities_max)):
        if cities_max[i] - cities_min[i] < 4000:
            ax.text(i, cities_min[i]+4000, '{}K'.format(k_format(cities_max[i])), rotation=0,
                    ha="center", va="center", bbox=dict(boxstyle="round", ec=(0., 0., 0.), fc=(0.7, 0.9, 1.), ))
            ax.text(i, cities_min[i], '{}K'.format(k_format(cities_min[i])), rotation=0,
                    ha="center", va="center", bbox=dict(boxstyle="round", ec=(1., 0.5, 0.5), fc=(1., 0.8, 0.8), ))
        else:
            ax.text(i, cities_max[i], '{}K'.format(k_format(cities_max[i])), rotation=0,
                    ha="center", va="center", bbox=dict(boxstyle="round", ec=(0., 0., 0.), fc=(0.7, 0.9, 1.), ))
            ax.text(i, cities_min[i], '{}K'.format(k_format(cities_min[i])), rotation=0,
                    ha="center", va="center", bbox=dict(boxstyle="round", ec=(1., 0.5, 0.5), fc=(1., 0.8, 0.8), ))
    ax.legend((p1[0], p2[0]), ('Minimum Salary', 'Maximum Salary'))
    # ax.set_ylabel('\n'.join(wrap(f'Plot for {no} MECs', 8))).set_rotation(0)
    ax.set_ylabel("Annual Salary", fontdict={'weight': 'medium', 'size': 12})
    ax.set_ylim(top=max(cities_max)+10000)
    ax.set_ylim(bottom=min(cities_min)//2)
    plt.title(f"Average Annual Salary Range for {job} in UK Cities", fontdict={'weight': 'medium', 'size': 12})
    plt.xticks(rotation=45)
    plt.subplots_adjust(bottom=0.16)
    plt.savefig(rf'C:\Users\Timothy Lam\Documents\Pycharm Projects\Chatbot\salary.png')
    plt.close()


def average_salary_graph_(job):
    path = rf'C:\Users\Timothy Lam\Documents\Pycharm Projects\Chatbot\salary.png'
    try:
        os.remove(path)
    except Exception as e:
        pass


    city_data = list(range(len(cities)))
    cities_min = list(range(len(cities)))
    cities_max = list(range(len(cities)))
    for i in cities:
        city_data[cities.index(i)] = pool.apply_async(average_salary_raw, (job, i))
    for i in range(len(city_data)):
        if city_data[i].get() == 0:
            cities_max[i] = 0
            cities_min[i] = 0
        else:
            result = city_data[i].get()
            cities_max[i] = result[1]
            cities_min[i] = result[0]
    #print(cities_max)
    #print(cities_min)
    salary_plot(cities_min, cities_max, job)
    display = f'<img src="salary.png?{time.time()}" alt=f"Average Salary graph for {job}" width="65%" height="65%">'
    say = f"The displayed graph contains the average salary range for {job} job in Top cities in UK"
    reply = {'display': display,
             'say': say}

    return reply


def average_salary_graph(job):
    global thread_result
    path = rf'C:\Users\Timothy Lam\Documents\Pycharm Projects\Chatbot\salary.png'
    try:
        os.remove(path)
    except Exception as e:
        pass

    cities = ["London", "Manchester", "Edinburgh", "Bristol", "Bath", "Birmingham", "Liverpool", "Glasgow"]
    city_data = []

    for i in cities:
        city_data.append(Thread(target=average_salary_raw, args=(job, i, cities.index(i))))
        city_data[-1].daemon = True
        city_data[-1].start()
    for _thread in city_data:
        _thread.join()
    cities_min,cities_max = thread_result

    # print(cities_max)
    # print(cities_min)
    salary_plot(cities_min, cities_max, job)
    display = f'<img src="salary.png?{time.time()}" alt=f"Average Salary graph for {job}" width="65%" height="65%">'
    say = f"The displayed graph contains the average salary range for {job} job in Top cities in UK"
    reply = {'display': display,
             'say': say}
    thread_result = [list(range(len(cities))), list(range(len(cities)))]
    return reply


def key_skills(job, place):  # TODO
    # find job key skills
    pass


































































