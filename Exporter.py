# -*- coding: utf-8 -*-
import sys,getopt,datetime,codecs
if sys.version_info[0] < 3:
    import got
else:
    import got3 as got

def main(argv):

	if len(argv) == 0:
		print('You must pass some parameters. Use \"-h\" to help.')
		return

	if len(argv) == 1 and argv[0] == '-h':
		f = open('exporter_help_text.txt', 'r')
		print f.read()
		f.close()

		return

	try:
		opts, args = getopt.getopt(argv, "", ("username=", "near=", "within=", "since=", "until=", "querysearch=", "toptweets", "maxtweets=", "output="))

		tweetCriteria = got.manager.TweetCriteria()
		outputFileName = "results"

		for opt,arg in opts:
			if opt == '--username':
				tweetCriteria.username = arg

			elif opt == '--since':
				tweetCriteria.since = arg

			elif opt == '--until':
				tweetCriteria.until = arg

			elif opt == '--querysearch':
				tweetCriteria.querySearch = arg

			elif opt == '--toptweets':
				tweetCriteria.topTweets = True

			elif opt == '--maxtweets':
				tweetCriteria.maxTweets = int(arg)
			
			elif opt == '--near':
				tweetCriteria.near = '"' + arg + '"'
			
			elif opt == '--within':
				tweetCriteria.within = '"' + arg + '"'

			elif opt == '--within':
				tweetCriteria.within = '"' + arg + '"'

			elif opt == '--output':
				outputFileName = arg
				
		outputFile = codecs.open('./results/' + outputFileName + '.txt', "w+", "utf-8")

		#outputFile.write('username;date;retweets;favorites;text;geo;mentions;hashtags;id;permalink')

		print('Searching...\n')

		def receiveBuffer(tweets):
			for t in tweets:
				#outputFile.write(('\n%s;%s;%d;%d;"%s";%s;%s;%s;"%s";%s' % (t.username, t.date.strftime("%Y-%m-%d %H:%M"), t.retweets, t.favorites, t.text, t.geo, t.mentions, t.hashtags, t.id, t.permalink)))

				outputFile.write('Usuario: %s\n' % t.username)
				outputFile.write('Fecha: %s\n' % t.date.strftime("%Y-%m-%d %H:%M"))
				outputFile.write('Retweets: %d\n' % t.retweets)
				outputFile.write('Favoritos: %d\n' % t.favorites)
				outputFile.write('Texto: "%s"\n' % t.text)
				outputFile.write('Locacion: %s\n' % t.geo)
				outputFile.write('Menciones: %s\n' % t.mentions)
				outputFile.write('Hashtags: %s\n' % t.hashtags)
				outputFile.write('ID: "%s"\n' % t.id)
				outputFile.write('URL: %s\n\n' % t.permalink)

			outputFile.flush()
			print('More %d saved on file...\n' % len(tweets))

		got.manager.TweetManager.getTweets(tweetCriteria, receiveBuffer)

	except arg:
		print('Arguments parser error, try -h' + arg)
	finally:
		outputFile.close()
		print('Done. Output file generated "%s".' % outputFileName)

if __name__ == '__main__':
	main(sys.argv[1:])
