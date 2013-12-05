#!/usr/bin/python
"""
Assignment06 Dist Systems CS4520
database stuff adapted from class
"""
import MySQLdb


def getConnection():
    conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='clubs', passwd='clubs', db='clubs')
    return conn


def getPersonById(ident):
    """ Returns in order: ident, name, description """
    conn = getConnection()
    cmd = "select ident, name, email from person where ident=%s"
    cursor = conn.cursor()
    cursor.execute(cmd, (ident,))
    pdata = cursor.fetchone()
    cursor.close()
    conn.close()
    return pdata


def getListOfPeople():
    """ Each tuple is (ident, name, email) """
    conn = getConnection()
    cmd = "select ident, name, email from person"
    cursor = conn.cursor()
    cursor.execute(cmd)
    rtval = cursor.fetchall()
    cursor.close()
    conn.close()
    return rtval


def getGroupById(ident):
    """ Returns in order: ident, name, description """
    conn = getConnection()
    cmd = "select ident, name, description from `group` where ident=%s"
    cursor = conn.cursor()
    cursor.execute(cmd, (ident,))
    pdata = cursor.fetchone()
    cursor.close()
    conn.close()
    return pdata


def getListOfGroups():
    """ Each tuple is (ident, name, email) """
    conn = getConnection()
    cmd = "select ident, name, description from `group`"
    cursor = conn.cursor()
    cursor.execute(cmd)
    rtval = cursor.fetchall()
    cursor.close()
    conn.close()
    return rtval


def getClubById(ident):
    """ Returns in order: ident, name, description, president_id  """
    conn = getConnection()
    cmd = "select ident, name, description, president_id from club where ident=%s"
    cursor = conn.cursor()
    cursor.execute(cmd, (ident,))
    pdata = cursor.fetchone()
    cursor.close()
    conn.close()
    return pdata


def getListOfClubs():
    """ Each tuple is (ident, name, email, president)  """
    conn = getConnection()
    cmd = "select ident, name, description, president_id from club"
    cursor = conn.cursor()
    cursor.execute(cmd)
    rtval = cursor.fetchall()
    cursor.close()
    conn.close()
    return rtval


def savePersonData(pdata):
    """ Save a person's data  """
    conn = getConnection()
    cmd = "update person set name=%s, email=%s where ident=%s"
    cursor = conn.cursor()
    cursor.execute(cmd, (pdata[1], pdata[2], pdata[0]))
    conn.commit()
    cursor.close()
    conn.close()


def saveGroupData(gdata):
    """ Save the group data """
    conn = getConnection()
    cmd = "update `group` set name=%s, description=%s where ident=%s"
    cursor = conn.cursor()
    cursor.execute(cmd, (gdata[1], gdata[2], gdata[0]))
    conn.commit()
    cursor.close()
    conn.close()


def getPersonByClub(ident):
    """ returns person ids  """
    conn = getConnection()
    cmd = "select person_id from member_of where club_id=%s"
    cursor = conn.cursor()
    cursor.execute(cmd, (ident,))
    pdata = cursor.fetchall()
    cursor.close()
    conn.close()
    return pdata


def getGroupByClub(club_id):
    """ returns group ids for club """
    conn = getConnection()
    cmd = "select group_id from belong_to where club_id=%s"
    cursor = conn.cursor()
    cursor.execute(cmd, (club_id,))
    gdata = cursor.fetchall()
    cursor.close()
    conn.close()
    return gdata

def updateClub(cdata):
    """ updates a clubs data (ident, name, desc, pres, grp)"""
    conn = getConnection()
    cmd = "update club set name=%s, description=%s, president_id=%s where ident=%s"
    cursor = conn.cursor()
    ident = cdata[0]
    cursor.execute(cmd, (cdata[1], cdata[2], cdata[3], ident))
    conn.commit()
    cursor.close()
    conn.close()


def saveNewClub(cdata):
    """ inserts new club which is (name, desc) """
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("select ident from club")
    identList = cursor.fetchall()
    ident = max(identList)
    ident = int(ident[0])+1
    cmd = "insert into club (ident, name, description) values (%s, %s, %s)"
    cursor.execute(cmd, (ident, cdata[0], cdata[1]))
    conn.commit()
    cursor.close()
    conn.close()
    return ident

def updateGroups(gdata):
    """ updates a groups membership for a group, by club_id, group_id"""
    conn = getConnection()
    cursor = conn.cursor()
    ident = gdata.pop(0)
    cmd1 = "delete from belong_to where club_id=%s"
    cursor.execute(cmd1, (ident, ))
    for g in gdata:
        cmd = "insert into belong_to set club_id=%s, group_id=%s"
        cursor.execute(cmd, (ident, g))
    conn.commit()
    cursor.close()
    conn.close()
