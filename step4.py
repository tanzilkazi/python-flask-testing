import redislite

# Open the connection to the mock Redis
r = redislite.StrictRedis()

# Try with a key-value
r.set('foo', 'bar')
print r.get('foo')

# Let's try hashes as well 
r.hmset('survey1',{'division':'ENT','state':'NSW','feedback':'hello world'})
r.hmset('survey2',{'division':'COMM','state':'NSW','feedback':'great'})
r.hmset('survey3',{'division':'ENT','state':'VIC','feedback':'awesome'})
response = "This is the Report\n"
for eachsurvey in r.keys('survey*'):
    response += "Division : " + r.hget(eachsurvey,'division') + "<br>\n"
    response += "State    : " + r.hget(eachsurvey,'state') + "<br>\n"
    response += "Feedback : " + r.hget(eachsurvey,'feedback') + "<br>\n"
    response += " ----------------------<br>\n"
print response




