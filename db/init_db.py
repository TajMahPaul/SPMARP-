import sqlite3

def main():
    conn = sqlite3.connect('surrey.db')
    c = conn.cursor()
    
    try:
        # Create tables
        c.execute('''CREATE TABLE IF NOT EXISTS waiting_points (WPid integer PRIMARY KEY AUTOINCREMENT, name text, FEDcode integer, FEDname text, lon real, lat real)''')
        c.execute('''CREATE TABLE IF NOT EXISTS demand_points (DAuid integer PRIMARY KEY, FEDcode integer, FEDname text, lon real, lat real, crime_index real, population_val real)''')
        # c.execute('''CREATE TABLE distances (w_id integer, d_id integer, distance_km real, time_m real)''')
        # c.execute('''CREATE TABLE optomization_output (n integer, alpha_i integer, )''')
    except Exception as e:
        raise(e)
    finally:
        # close connection and cursor
        c.close()
        conn.close()

if __name__ == "__main__":
    main()