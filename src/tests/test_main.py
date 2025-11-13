from cinema_de_la_cite.main import main

def test_main_output(capsys):
    """Test que la fonction main() affiche le bon message."""
    main()  # appelle la fonction
    captured = capsys.readouterr()  # capture la sortie console
    assert captured.out.strip() == "Hello from cinema-de-la-cite!"