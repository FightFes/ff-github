package main

import (
	"fmt"
	"net/url"

	"./screens"
	"fyne.io/fyne"
	"fyne.io/fyne/app"
	"fyne.io/fyne/canvas"
	"fyne.io/fyne/cmd/fyne_demo/data"
	"fyne.io/fyne/layout"
	"fyne.io/fyne/theme"
	"fyne.io/fyne/widget"
)

const preferenceCurrentTab = "currentTab"

func welcomeScreen(test_app fyne.App) fyne.CanvasObject {
	logo := canvas.NewImageFromResource(data.FyneScene)
	logo.SetMinSize(fyne.NewSize(228, 167))

	link, err := url.Parse("https://fyne.io/")
	if err != nil {
		fyne.LogError("Could not parse URL", err)
	}

	return widget.NewVBox(
		widget.NewLabelWithStyle("Welcome to the Fyne toolkit demo app", fyne.TextAlignCenter, fyne.TextStyle{Bold: true}),
		layout.NewSpacer(),
		widget.NewHBox(layout.NewSpacer(), logo, layout.NewSpacer()),
		widget.NewHyperlinkWithStyle("fyne.io", link, fyne.TextAlignCenter, fyne.TextStyle{}),
		layout.NewSpacer(),

		widget.NewGroup("Theme",
			fyne.NewContainerWithLayout(layout.NewGridLayout(2),
				widget.NewButton("Dark", func() {
					test_app.Settings().SetTheme(theme.DarkTheme())
				}),
				widget.NewButton("Light", func() {
					test_app.Settings().SetTheme(theme.LightTheme())
				}),
			),
		),
	)
}

func main() {
	test_app := app.NewWithID("io.fyne.test")
	test_app.SetIcon(theme.FyneLogo())

	main_window := test_app.NewWindow("test")
	main_window.SetMainMenu(
		fyne.NewMainMenu(
			fyne.NewMenu("File",
				fyne.NewMenuItem("New", func() { fmt.Println("Menu New") }),
			),
			fyne.NewMenu("Edit",
				fyne.NewMenuItem("Cut", func() { fmt.Println("Menu Cut") }),
				fyne.NewMenuItem("Copy", func() { fmt.Println("Menu Copy") }),
				fyne.NewMenuItem("Paste", func() { fmt.Println("Menu Paste") }),
			)))
	main_window.SetMaster()

	tabs := widget.NewTabContainer(
		widget.NewTabItemWithIcon("Welcome", theme.HomeIcon(), welcomeScreen(test_app)),
		widget.NewTabItemWithIcon("test", theme.DocumentCreateIcon(), screens.TestScreen()))
	tabs.SetTabLocation(widget.TabLocationLeading)
	tabs.SelectTabIndex(test_app.Preferences().Int(preferenceCurrentTab))
	main_window.SetContent(tabs)

	main_window.ShowAndRun()

	test_app.Preferences().SetInt(preferenceCurrentTab, tabs.CurrentTabIndex())
}
